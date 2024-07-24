>>> import PyPDF2
>>> minutesFile = open('meetingminutes.pdf', 'rb')
>>> pdfReader = PyPDF2.PdfFileReader(minutesFile)
>>> minutesFirstPage = pdfReader.getPage(0)
>>> pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
>>> minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
>>> pdfWriter = PyPDF2.PdfFileWriter()
>>> pdfWriter.addPage(minutesFirstPage)
>>> for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
>>> resultPdfFile = open('watermarkedCover.pdf', 'wb')
>>> pdfWriter.write(resultPdfFile)
>>> minutesFile.close()
>>> resultPdfFile.close()

# Here we make a PdfFileReader object of meetingminutes.pdf. We call
# getPage(0) to get a Page object for the first page and store this object in
# minutesFirstPage. We then make a PdfFileReader object for watermark
# .pdf w and call mergePage() on minutesFirstPage. The argument we pass
# to mergePage() is a Page object for the first page of watermark.pdf.
# Now that we’ve called mergePage() on minutesFirstPage, minutesFirstPage
# represents the water marked first page. We make a PdfFileWriter object 
# and add the watermarked first page. Then we loop through the rest of
# the pages in meetingminutes.pdf and add them to the PdfFileWriter object.
# Finally, we open a new PDF called watermarkedCover.pdf and write the con-
# tents of the PdfFileWriter to the new PDF.
