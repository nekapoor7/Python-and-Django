"""HOW TO CONVERT .PDF TO .TXT USING PYTHON"""
import PyPDF2
pdffileobj = open('RentalDocument.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(pdffileobj)
