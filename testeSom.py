'''from gtts import gTTS
import os

# Texto que você quer que seja lido
texto = "Pode começar"

# Converte o texto para fala
tts = gTTS(text=texto, lang='pt')

# Salva o arquivo de áudio
tts.save("voz.mp3")

# Reproduz o arquivo de áudio
os.system("voz.mp3")'''
from playsound import playsound
playsound('voz.mp3')

