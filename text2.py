import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

image_names = [
    '1-78',
    '79-156',
    '80-240',
    '241-329',
    '330-419',
    '420-500'
]

for name in image_names:
    pdf = pytesseract.image_to_pdf_or_hocr(f'screenshots/{name}.png', extension='pdf')
    with open(f'{name}.pdf', 'w+b') as f:
        f.write(pdf)