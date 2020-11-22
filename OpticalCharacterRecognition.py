import os
from gtts import gTTS 
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

image = cv2.imread('1.png')
text = pytesseract.image_to_string(image)
print(text)

processed_text = ""

for i in text.split():
    processed_text += i + " "

print(processed_text)

tts = gTTS(processed_text)
tts.save("hi.mp3")

os.system("hi.mp3")


