import os
import qrcode
from PIL import Image

def generateQRCodeWithLogo(data, outputFolder, filename, logoPath):
    # Cria a pasta de saída se não existir
    os.makedirs(outputFolder, exist_ok=True)
    
    # Configura o QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Cria imagem do QR code
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    logo = Image.open(logoPath)
    
    # Calcula tamanho máximo da logo (20% do QR code)
    max_logo_size = min(img.size) // 5
    logo.thumbnail((max_logo_size, max_logo_size), Image.LANCZOS)
    
    # Calcula posição para centralizar a logo
    pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    
    # Cola a logo no QR code
    img.paste(logo, pos)
    
    # Salva imagem
    img.save(os.path.join(outputFolder, f"{filename}.png"))

def batchGenerateQRCodeWithLogo(outputFolder, logoPath):
    dataList = []

    for i in range(1, 11): # Gera 10 IDs
        dataList.append({
            "data": f"ID{i}",
            "filename": f"QRcode-{i}"
        })

    for item in dataList:
        print(f"Arquivo: {item['filename']}")
        print(f"Dado: {item['data']}")

        generateQRCodeWithLogo(
            data=item['data'],
            outputFolder=outputFolder,
            filename=item['filename'],
            logoPath=logoPath
        )


outputFolder = "qrcodes"

logoPath = "logoPath"

batchGenerateQRCodeWithLogo(outputFolder, logoPath)

print(f"QR codes gerados na pasta '{outputFolder}'")