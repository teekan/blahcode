import sys
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

start_page = int(sys.argv[3])
end_page = int(sys.argv[4])
output_pdf = sys.argv[2]
input_pdf = sys.argv[1]

pdf = PdfFileReader(str(input_pdf))

pdf_writer = PdfFileWriter()

for x in range(start_page, end_page + 1):
    page = pdf.getPage(x-1)
    print(page.getContents())
    print(page.extractText())
    pdf_writer.addPage(page)

with Path(output_pdf).open(mode="wb") as output_file:
    pdf_writer.write(output_file)
