from glob import glob
from pikepdf import Pdf

nuevo_pdf=Pdf.new()

for archivo in glob("*.pdf"):
    pdf_raiz=Pdf.open(archivo)
    nuevo_pdf.pages.extend(pdf_raiz.pages)

nuevo_pdf.save("pdfs_unidos.pdf")