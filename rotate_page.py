import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

# Here we use getPage(0) to select the first page of the PDF, and then
# we call rotateClockwise(90) on that page. We write a new PDF with the
# rotated page and save it as rotatedPage.pdf.
# The resulting PDF will have one page, rotated 90 degrees clock-
# wise, as in Figure 13-2. The return values from rotateClockwise() and
# rotateCounterClockwise() contain a lot of information that you can ignore.