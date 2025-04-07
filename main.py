from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from spellchecker import SpellChecker
import os

# Caminhos
pdf_path = r"C:/Fontes/proc_images_2025_1/ExemploOCR/MussumIpsum.pdf"
pasta_paginas = "paginas"
arquivo_txt = "texto_extraido_corrigido.txt"

# Criar pasta se não existir
os.makedirs(pasta_paginas, exist_ok=True)

# Converter PDF para imagens
imagens = convert_from_path(pdf_path)
spell = SpellChecker(language='pt')  # Dicionário em português

texto_total = ""

for i, img in enumerate(imagens):
    caminho_imagem = os.path.join(pasta_paginas, f"pagina{i}.jpg")
    img.save(caminho_imagem, "JPEG")

    # OCR
    texto = pytesseract.image_to_string(img, lang="por")

    # Correção ortográfica (simples, palavra a palavra)
    palavras = texto.split()
    corrigidas = []
    for palavra in palavras:
        if palavra.isalpha():
            palavra_corrigida = spell.correction(palavra)
            corrigidas.append(palavra_corrigida)
        else:
            corrigidas.append(palavra)

    texto_corrigido = " ".join(corrigidas)
    texto_total += f"\n--- Página {i} ---\n{texto_corrigido}\n"

# Salvar tudo em um .txt
with open(arquivo_txt, "w", encoding="utf-8") as f:
    f.write(texto_total)

print(f"\n✅ Texto extraído, corrigido e salvo em '{arquivo_txt}'")
