"""Uso: python hacer_qr.py https://TU_USUARIO.github.io/NOMBRE_REPO/
Genera qr_beatriz.png (QR granate con corazón en el centro, listo para imprimir)."""
import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont

url = sys.argv[1]
qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=20, border=3)
qr.add_data(url); qr.make(fit=True)
img = qr.make_image(fill_color="#7a1f2e", back_color="white").convert("RGB")

# corazón en el centro (ECC nivel H tolera ~30% tapado)
w = img.width; r = w // 9
d = ImageDraw.Draw(img)
cx, cy = w // 2, w // 2
d.ellipse((cx - r - 8, cy - r - 8, cx + r + 8, cy + r + 8), fill="white")
try:
    f = ImageFont.truetype("seguisym.ttf", int(r * 1.5))
except OSError:
    f = ImageFont.load_default(size=int(r * 1.5))
d.text((cx, cy), "♥", font=f, fill="#7a1f2e", anchor="mm")

# texto debajo
canvas = Image.new("RGB", (w, w + 140), "white"); canvas.paste(img, (0, 0))
d = ImageDraw.Draw(canvas)
try:
    f2 = ImageFont.truetype("georgiai.ttf", 64)
except OSError:
    f2 = ImageFont.load_default(size=64)
d.text((w // 2, w + 50), "Escanéame, Beatriz", font=f2, fill="#7a1f2e", anchor="mm")
canvas.save("qr_beatriz.png")
print("OK -> qr_beatriz.png  ", url)
