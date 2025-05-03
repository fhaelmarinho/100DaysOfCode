# ✨ Desafio 100 Dias de Código - Dia 4/100 💻

import qrcode
import cv2

msg = 'Hello World!'

qr = qrcode.QRCode(version=1, box_size=6, border=2)
qr.add_data(msg)
qr.make()

img = qr.make_image(fill_color='black', back_color='white')
file_path = 'qrcode.png'
img.save('qrcode.png')
img.show()

image = cv2.imread(file_path)
detector = cv2.QRCodeDetector()
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
if vertices_array is not None:
    print(f"Data: {data}")
else:
    print("Data failure")
