"""Gera os clipes da voz do pistoleiro (pasta voz/) a partir dos trechos de fala do nav.js.

Uso: python3 tools/gerar_voz.py caminho/pt-br-edresson-low.onnx
Requer: piper-tts, ffmpeg, node. A voz base é o modelo Piper "edresson" (pt-BR), treinado no
TTS-Portuguese Corpus de Edresson Casanova (CC BY 4.0). O ffmpeg rebaixa o tom, desacelera a fala
e dá corpo e aspereza ao timbre.
"""
import json, os, subprocess, sys, tempfile, wave
from piper import PiperVoice, SynthesisConfig

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, 'voz')
FILTER = ",".join([
    "silenceremove=start_periods=1:start_threshold=-45dB",
    "areverse", "silenceremove=start_periods=1:start_threshold=-45dB", "areverse",
    "asetrate=16000*0.87", "aresample=24000",             # ~2,4 semitons abaixo e fala 13% mais lenta
    "highpass=f=70", "lowpass=f=6800",
    "equalizer=f=140:t=q:w=1.2:g=5",                       # peito
    "equalizer=f=2600:t=q:w=1.5:g=-2",
    "acompressor=threshold=-18dB:ratio=3:attack=5:release=80",
    "volume=2.2", "asoftclip=type=tanh",                   # aspereza leve
    "aecho=0.8:0.4:35:0.10",
    "apad=pad_dur=0.05",
    "loudnorm=I=-15:TP=-1.5:LRA=7",
])

def main(model):
    nav = os.path.join(BASE, 'nav.js')
    js = f"const N=require({json.dumps(nav)});console.log(JSON.stringify(N.allChunks().map(t=>[N.slug(t),t])))"
    chunks = json.loads(subprocess.check_output(['node', '-e', js]))
    os.makedirs(OUT, exist_ok=True)
    voice = PiperVoice.load(model)
    cfg = SynthesisConfig(length_scale=1.0, noise_scale=0.6, noise_w_scale=0.7)
    ids = []
    with tempfile.TemporaryDirectory() as tmp:
        for cid, text in chunks:
            raw = os.path.join(tmp, cid + '.wav')
            with wave.open(raw, 'wb') as w:
                voice.synthesize_wav(text, w, syn_config=cfg)
            dst = os.path.join(OUT, cid + '.mp3')
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', raw, '-af', FILTER, '-ac', '1', '-ar', '24000',
                            '-b:a', '48k', dst], check=True)
            ids.append(cid)
    with open(os.path.join(OUT, 'manifest.json'), 'w') as f:
        json.dump({'versao': 1, 'clipes': sorted(ids)}, f)
    print(len(ids), 'clipes gerados em', OUT)

if __name__ == '__main__':
    main(sys.argv[1])
