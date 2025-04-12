# Extração e Correção Ortográfica de Texto em PDF via OCR

# Descrição
Este projeto realiza a extração de texto de um arquivo PDF com uso de OCR (Reconhecimento Óptico de Caracteres) e aplica correções ortográficas automáticas utilizando o `pyspellchecker`.
Ideal para automatizar a leitura de documentos escaneados com erros ortográficos comuns.

## Etapas do Processo
1. O PDF é convertido em imagens (uma por página) usando `pdf2image`.
2. O `pytesseract` extrai o texto das imagens.
3. Cada palavra do texto é verificada e corrigida quando necessário com `pyspellchecker`.
4. São salvos dois arquivos `.txt`: um com o texto original, outro com o texto corrigido.
5. Para converter um outro PDF em texto aplicar a correção ortografica basta configurar o caminho do arquivo para o novo arquivo.

### Pré-requisitos
- Python 3.8+
- Tesseract OCR instalado (Windows: https://github.com/tesseract-ocr/tesseract)
- [pdf2image](https://pypi.org/project/pdf2image/) - Conversão de PDFs para imagens
- [Pillow (PIL)](https://pypi.org/project/Pillow/) - Manipulação de imagens
- [pyspellchecker](https://pypi.org/project/pyspellchecker/) - Correção ortográfica básica
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (instalado no sistema)
- Poppler (para leitura de PDFs)

# Resultados

As imagens convertidas serão salvas na pasta paginas/.

O texto original será salvo em texto_original.txt.

O texto corrigido será salvo em texto_corrigido.txt.



