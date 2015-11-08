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
        self.filename = filename

        fp = open(self.filename, 'rb')
        parser = PDFParser(fp)
        self.doc = PDFDocument()
        parser.set_document(self.doc)
        self.doc.set_parser(parser)
        self.doc.initialize('')
        
    def writeToTxt(self):
        text = self.getString()
        txtFile = open(self.filename.replace(".pdf", ".txt"), "w")
        txtFile.write(text.encode('ascii','replace').decode("utf-8"))
        txtFile.close()

    def getString(self):
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        string = StringIO()
        device = TextConverter(rsrcmgr, string, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in self.doc.get_pages():
            interpreter.process_page(page)
        return string.getvalue()
