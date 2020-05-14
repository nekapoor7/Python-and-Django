"""TEXT TO SPEECH USING PYTHON (Create your own audio book)"""
from gtts import gTTS
import os

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt", 'r', encoding='utf-8') as file1:
    data = file1.read()

lang = 'en'
audio=gTTS(text=data,lang='en',slow=False)

audio.save("audio_file.wav")

os.system("audio_file.wav")