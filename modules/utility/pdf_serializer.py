'''
PDF read method here
'''

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, HTMLConverter, XMLConverter
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from io import StringIO
from ChunkParser import ChunkParser

class PdfSerializer(object):
    def __init__(self, filename):
        self.filename = filename

    def getText(self):
        '''Convert PDF to text'''
        # reference to http://stackoverflow.com/questions/26413216/pdfminer3k-has-no-method-named-create-pages-in-pdfpage
        fp = open(self.filename, 'rb')
        parser = PDFParser(fp)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize('')
        rsrcmgr = PDFResourceManager()
        txtFile = open(self.filename.replace(".pdf", ".txt"), "w")
        laparams = LAParams()
        #string = StringIO()
        device = TextConverter(rsrcmgr, txtFile, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.

        
        
        for page in doc.get_pages():
            interpreter.process_page(page)

        txtFile.close()
        #print(string.getvalue())
        #outlines = doc.get_outlines()
        #for (level,title,dest,a,se) in outlines:
        #    print (level, title)


        #chunhow = ChunkParser.tokenize(string.getvalue())
        #print(chunhow)
        
names = {"1.pdf", "2.pdf", "3.pdf", "4.pdf", "5.pdf", "6.pdf", "7.pdf", "8.pdf", "9.pdf"}
for name in names:
    print(name)
    convert = PdfSerializer(name)
    convert.getText()
#print(convert.str)
