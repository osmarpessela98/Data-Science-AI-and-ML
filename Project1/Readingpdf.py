import PyPDF2

#Aploud the pdf
pdfFileObj = open('mepdf.pdf', 'rb')

#Reader
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Fist Page
pageObj = pdfReader.getPage(0)

#Put Out
text = pageObj.extractText()

#Print
print (text)