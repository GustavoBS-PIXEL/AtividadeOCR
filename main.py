from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from spellchecker import SpellChecker
import os
import re

# (Opcional) Caminho do Tesseract, necessário em alguns sistemas Windows
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# === Configurações ===
pdf_path = r"C:/Fontes/proc_images_2025_1/AtividadeOCR/teste.pdf"
pasta_paginas = "paginas"
arquivo_corrigido = "texto_corrigido.txt"
arquivo_original = "texto_original.txt"

# Criar pasta de saída se não existir
os.makedirs(pasta_paginas, exist_ok=True)

# Inicializar corretor ortográfico em português
spell = SpellChecker(language='pt')

# === Função para corrigir texto extraído ===
def corrigir_texto(texto):
    palavras = texto.split()
    corrigidas = []

    for palavra in palavras:
        # Remove pontuação para verificar ortografia
        limpa = re.sub(r'[^\wÀ-ÿ]', '', palavra)

        if limpa.isalpha():
            # Corrige apenas palavras desconhecidas
            if limpa.lower() in spell:
                corrigidas.append(palavra)
            else:
                sugestao = spell.correction(limpa)
                palavra_corrigida = palavra.replace(limpa, sugestao)
                corrigidas.append(palavra_corrigida)
        else:
            corrigidas.append(palavra)

    return " ".join(corrigidas)

# === Processo Principal ===
texto_total_original = ""
texto_total_corrigido = ""

try:
    imagens = convert_from_path(pdf_path)
except Exception as e:
    print(f"Erro ao converter PDF para imagens: {e}")
    exit()

for i, img in enumerate(imagens):
    caminho_img = os.path.join(pasta_paginas, f"pagina{i}.jpg")
    img.save(caminho_img, "JPEG")

    # Extração OCR
    texto_ocr = pytesseract.image_to_string(img, lang="por")
    texto_corrigido = corrigir_texto(texto_ocr)
    texto_total_original += f"\n--- Página {i} ---\n{texto_ocr.strip()}\n"
    texto_total_corrigido += f"\n--- Página {i} ---\n{texto_corrigido.strip()}\n"

# === Salvar resultados ===
with open(arquivo_original, "w", encoding="utf-8") as f:
    f.write(texto_total_original)

with open(arquivo_corrigido, "w", encoding="utf-8") as f:
    f.write(texto_total_corrigido)

print(f"\n✅ Texto original salvo em '{arquivo_original}'")
print(f"✅ Texto corrigido salvo em '{arquivo_corrigido}'")