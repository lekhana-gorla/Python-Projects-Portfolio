import pypdf
import gtts
from pypdf import PdfReader
reader = PdfReader("Python for Everybody.pdf")
text=" "
for page in reader.pages:
    text+=page.extract_text()


from gtts import gTTS
tts = gTTS(text, lang='en')
tts.save('Python for Everybody.mp3')




