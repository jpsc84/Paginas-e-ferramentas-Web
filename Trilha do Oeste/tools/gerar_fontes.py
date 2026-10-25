"""Gera os glifos SDF (formato .pbf do MapLibre) das fontes do mapa na pasta fonts/.

Uso: python3 tools/gerar_fontes.py <pasta com os .woff2 do Fontsource>
Requer: fonttools, brotli, freetype-py, numpy, scipy.
Fontes livres (SIL Open Font License): Libre Franklin e Alegreya.
"""
import io, os, sys
import numpy as np
import freetype
from fontTools.ttLib import TTFont
from scipy.ndimage import distance_transform_edt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, 'fonts')
SIZE, BUFFER, RADIUS, CUTOFF, OS = 24, 3, 8, 0.25, 4   # padrão do MapLibre; OS = superamostragem

STACKS = {
    'TrilhaCidade': ['libre-franklin-latin-800-normal', 'libre-franklin-latin-ext-800-normal'],
    'TrilhaRegiao': ['alegreya-latin-900-normal', 'alegreya-latin-ext-900-normal'],
    'TrilhaLugar':  ['alegreya-latin-700-italic', 'alegreya-latin-ext-700-italic'],
    'TrilhaRua':    ['alegreya-latin-400-italic', 'alegreya-latin-ext-400-italic'],
}
RANGES = [(0, 255), (256, 511), (8192, 8447)]

# ---- protobuf mínimo ----
def varint(n):
    out = bytearray()
    while True:
        b = n & 0x7F; n >>= 7
        out.append(b | (0x80 if n else 0))
        if not n: return bytes(out)
def key(field, wt): return varint((field << 3) | wt)
def f_varint(field, n): return key(field, 0) + varint(n)
def f_sint(field, n): return key(field, 0) + varint((n << 1) ^ (n >> 31) if n < 0 else n << 1)
def f_bytes(field, b): return key(field, 2) + varint(len(b)) + b

def load_faces(names, src):
    faces = []
    for n in names:
        f = TTFont(os.path.join(src, n + '.woff2'))
        f.flavor = None
        buf = io.BytesIO(); f.save(buf)
        face = freetype.Face(io.BytesIO(buf.getvalue()))
        face.set_pixel_sizes(0, SIZE * OS)
        faces.append(face)
    return faces

def glyph_msg(face, code):
    face.load_char(chr(code), freetype.FT_LOAD_RENDER | freetype.FT_LOAD_TARGET_NORMAL)
    g = face.glyph; bm = g.bitmap
    advance = int(round(g.advance.x / 64 / OS))
    msg = f_varint(1, code)
    if bm.width == 0 or bm.rows == 0:
        return msg + f_varint(3, 0) + f_varint(4, 0) + f_sint(5, 0) + f_sint(6, 0) + f_varint(7, advance)
    hi = np.array(bm.buffer, dtype=np.uint8).reshape(bm.rows, bm.pitch)[:, :bm.width] / 255.0
    left = int(np.floor(g.bitmap_left / OS)); top = int(np.ceil(g.bitmap_top / OS))
    ox = g.bitmap_left - left * OS; oy = top * OS - g.bitmap_top
    w = int(np.ceil((bm.width + ox) / OS)); h = int(np.ceil((bm.rows + oy) / OS))
    W, H = w + 2 * BUFFER, h + 2 * BUFFER
    canvas = np.zeros((H * OS, W * OS))
    y0, x0 = BUFFER * OS + oy, BUFFER * OS + ox
    canvas[y0:y0 + bm.rows, x0:x0 + bm.width] = hi
    inside = canvas >= 0.5
    d_out = distance_transform_edt(~inside)
    d_in = distance_transform_edt(inside)
    signed = (d_out - d_in) / OS                     # positivo fora do glifo, em pixels de 24 px
    c = OS // 2
    sample = signed[c::OS, c::OS][:H, :W]
    vals = np.clip(np.round(255 - 255 * (sample / RADIUS + CUTOFF)), 0, 255).astype(np.uint8)
    return (msg + f_bytes(2, vals.tobytes()) + f_varint(3, w) + f_varint(4, h)
            + f_sint(5, left) + f_sint(6, top) + f_varint(7, advance))

def main(src):
    for name, files in STACKS.items():
        faces = load_faces(files, src)
        cmaps = [set(TTFont(os.path.join(src, n + '.woff2')).getBestCmap().keys()) for n in files]
        os.makedirs(os.path.join(OUT, name), exist_ok=True)
        total = 0
        for a, b in RANGES:
            glyphs = b''
            for code in range(a, b + 1):
                for face, cmap in zip(faces, cmaps):
                    if code in cmap:
                        glyphs += f_bytes(3, glyph_msg(face, code)); total += 1
                        break
            stack = f_bytes(1, name.encode()) + f_bytes(2, f'{a}-{b}'.encode()) + glyphs
            with open(os.path.join(OUT, name, f'{a}-{b}.pbf'), 'wb') as fh:
                fh.write(f_bytes(1, stack))
        print(name, total, 'glifos')

if __name__ == '__main__':
    main(sys.argv[1])
