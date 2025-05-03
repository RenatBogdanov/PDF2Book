import sys
from PyPDF2 import PdfReader, PdfWriter

def pdf_to_brochure(input_pdf, output_pdf):
    # Открываем входной PDF-файл
    pdf_reader = PdfReader(input_pdf)
    num_pages = len(pdf_reader.pages)

    # Создаем выходной PDF-файл
    pdf_writer = PdfWriter()

    # Переставляем страницы в формат брошюры
    pages = []
    for i in range(num_pages // 2):
        pages.append(pdf_reader.pages[num_pages - 1 - i])
        pages.append(pdf_reader.pages[i])

    # Если количество страниц нечетное, добавляем последнюю страницу
    if num_pages % 2!= 0:
        pages.append(pdf_reader.pages[num_pages // 2])

    # Меняем местами каждую 3 и 4 страницу
    for i in range(0, len(pages), 4):
        if i + 3 < len(pages):
            pages[i+2], pages[i+3] = pages[i+3], pages[i+2]

    # Записываем страницы в выходной PDF-файл
    for page in pages:
        pdf_writer.add_page(page)

    # Записываем выходной PDF-файл
    with open(output_pdf, 'wb') as f:
        pdf_writer.write(f)

if __name__ == '__main__':
    if len(sys.argv)!= 3:
        print("Использование: python pdf2book.py <input_pdf> <output_pdf>")
    else:
        input_pdf = sys.argv[1]
        output_pdf = sys.argv[2]
        pdf_to_brochure(input_pdf, output_pdf)
        print("Готово!")