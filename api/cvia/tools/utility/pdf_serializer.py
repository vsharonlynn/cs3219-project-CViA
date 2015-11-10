'''
PDF read method here
'''

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, HTMLConverter, XMLConverter
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from io import StringIO

class PdfSerializer(object):
    def __init__(self, filename):
        self.__filename = filename

        fp = open(self.__filename, 'rb')
        parser = PDFParser(fp)
        self.__doc = PDFDocument()
        parser.set_document(self.__doc)
        self.__doc.set_parser(parser)
        self.__doc.initialize('')

    def writeToTxt(self):
        text = self.getString()
        txtFile = open(self.__filename.replace(".pdf", ".txt"), "w")
        txtFile.write(text.encode('ascii','replace').decode("utf-8"))
        txtFile.close()

    def getString(self):
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        string = StringIO()
        device = TextConverter(rsrcmgr, string, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in self.__doc.get_pages():
            interpreter.process_page(page)
        return string.getvalue()

#test = PdfSerializer("t.pdf")
#print(test.getString())
