import qrcode
from PIL import Image

# URL вашей AR-страницы (после хостинга)
ar_url = "https://margaritasi.github.io/VR/"

# Создание QR-кода
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(ar_url)
qr.make(fit=True)

# Генерация изображения
img = qr.make_image(fill_color="black", back_color="white")
img.save("ar_qr_code.png")

print(f"QR-код создан! Ведет на: {ar_url}")