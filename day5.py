# ✨ Desafio 100 Dias de Código - Dia 5/100 💻

from rembg import remove
from PIL import Image
import io

input_path = 'perfil.png'
output_path = 'output.png'

input_image = Image.open(input_path)

# Converte a imagem para bytes
input_bytes = io.BytesIO()
input_image.save(input_bytes, format='PNG')
input_bytes = input_bytes.getvalue()

output_bytes = remove(input_bytes)

# Converte os bytes de volta para uma imagem PIL
output_image = Image.open(io.BytesIO(output_bytes))

# Salva e exibe a imagem com o fundo removido
output_image.save(output_path)
output_image.show()
