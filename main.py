import pyttsx3
import PyPDF2
book = open('pride-and-prejudice.pdf', 'rb')
pdfReader= PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(2, pages):
    page = pdfReader.getPage(2)
    txt = page.extractText()
    speaker.say(txt)
speaker.runAndWait()