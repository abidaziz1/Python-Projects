import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages   # 19 or like that
pageObj = pdfReader.getPage(0)
pageObj.extractText()

# Decrypting PDFs
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted # True or False
pdfReader.getPage(0)
pdfReader.decrypt('rosebud') # rosebud is the password here
pageObj = pdfReader.getPage(0)
# Note that the decrypt() method decrypts only the PdfFileReader object, not
# the actual PDF file. After your program terminates, the file on your hard
# drive remains encrypted. Your program will have to call decrypt() again the
# next time it is run.


# PyPDF2 doesn’t allow you to directly edit a PDF. Instead, you have to
# create a new PDF and then copy content over from an existing document.
# The examples in this section will follow this general approach:
# 1. Open one or more existing PDFs (the source PDFs) into PdfFileReader
# objects.
# 2. Create a new PdfFileWriter object.
# 3. Copy pages from the PdfFileReader objects into the PdfFileWriter object.
# 4. Finally, use the PdfFileWriter object to write the output PDF.




# Copying Pages
>>> import PyPDF2
>>> pdf1File = open('meetingminutes.pdf', 'rb')
>>> pdf2File = open('meetingminutes2.pdf', 'rb')
>>> pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
>>> pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
>>> pdfWriter = PyPDF2.PdfFileWriter()
>>> for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
>>> for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
>>> pdfOutputFile = open('combinedminutes.pdf', 'wb')
>>> pdfWriter.write(pdfOutputFile)
>>> pdfOutputFile.close()
>>> pdf1File.close()
>>> pdf2File.close()
# Open both PDF files in read binary mode and store the two resulting
# File objects in pdf1File and pdf2File. Call PyPDF2.PdfFileReader() and pass
# it pdf1File to get a PdfFileReader object for meetingminutes.pdf. Call it again
# and pass it pdf2File to get a PdfFileReader object for meetingminutes2.pdf.
# Then create a new PdfFileWriter object, which represents a blank PDF document.
# Next, copy all the pages from the two source PDFs and add them
# to the PdfFileWriter object. Get the Page object by calling getPage() on a
# PdfFileReader object. Then pass that Page object to your PdfFileWriter’s
# addPage() method. These steps are done first for pdf1Reader and then
# again for pdf2Reader. When you’re done copying pages, write a new PDF
# called combinedminutes.pdf by passing a File object to the PdfFileWriter’s
# write() method.
