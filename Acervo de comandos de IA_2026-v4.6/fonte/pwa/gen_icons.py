"""Gera os ícones do app (PNG e ICO) a partir de icon.svg e maskable.svg. Saída em ./icons/."""
import os
from playwright.sync_api import sync_playwright
from PIL import Image
os.makedirs("icons", exist_ok=True)
jobs = [("icon.svg", 512, "icon-512.png"), ("icon.svg", 192, "icon-192.png"), ("maskable.svg", 512, "maskable-512.png"),
        ("maskable.svg", 192, "maskable-192.png"), ("maskable.svg", 180, "apple-touch-icon.png"), ("icon.svg", 64, "_64.png")]
with sync_playwright() as p:
    b = p.chromium.launch()
    for svg, size, out in jobs:
        pg = b.new_page(viewport={"width": size, "height": size})
        pg.set_content('<html><body style="margin:0">%s</body></html>' % open(svg).read().replace("<svg ", "<svg width=%d height=%d " % (size, size), 1))
        pg.screenshot(path="icons/" + out, omit_background=True, clip={"x": 0, "y": 0, "width": size, "height": size}); pg.close()
    b.close()
Image.open("icons/_64.png").save("icons/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)]); os.remove("icons/_64.png")
import shutil; shutil.copy("icon.svg", "icons/icon.svg")
print("ícones gerados:", sorted(os.listdir("icons")))
