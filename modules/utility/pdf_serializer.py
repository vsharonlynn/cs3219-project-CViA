'''
PDF read method here
'''
from PyPDF2 import PdfFileReader

class PdfSerializer(object):
    def __init__(self, filename):
        self.filename = filename

    def getText(self):
        '''Convert PDF to text'''
        pdfFile = PdfFileReader(open(self.filename, "rb"))
        pages = pdfFile.getNumPages()
        txtFile = open(self.filename.replace(".pdf", ".txt"), "w")

        for x in range(0, pages):
            page = pdfFile.getPage(x).extractText()
            txtFile.write(page.encode('ascii','ignore').decode("utf-8") )

        txtFile.close()
        
        pass

convert = PdfSerializer("t.pdf")
convert.getText()
