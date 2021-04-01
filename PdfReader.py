import pyttsx3
import PyPDF2

pdf = open('AOI.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
pages = pdfReader.numPages
print(pages)

speak = pyttsx3.init()
speak.say("Hello")
speak.say("Welcoming you to PDF Reader")

for i in range(0,pages):
    Page = pdfReader.getPage(i)
    Read = Page.extractText()
    speak.say(Read)
    speak.runAndWait()
