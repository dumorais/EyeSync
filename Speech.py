import pyperclip as pc
import speech_recognition as sr
import pyautogui
from playsound import playsound

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        print("Você disse: " + frase)
        pc.copy(frase)
        pyautogui.hotkey('ctrl', 'v')
      #  pyautogui.press('enter')
    except sr.UnkownValueError:
        print("Não entendi")
    return 

def switch_to_portuguese():
    ouvir_microfone()


recognizer = sr.Recognizer()
mic = sr.Microphone()

listening_in_portuguese = False

def StartListen():
    with mic as source:
        print("Aguardando a palavra-chave em inglês...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Pronto! Pode falar...")

        while True:
            audio = recognizer.listen(source)
            
            try:
                speech = recognizer.recognize_google(audio, language="en-US")
                print(f"Você disse em inglês: {speech}")

                if "icing" in speech or "ITestando pesquisa think" in speech or "eye sync" in speech:
                    playsound('voz.mp3')
                    switch_to_portuguese()
                    listening_in_portuguese = True 

            except sr.UnknownValueError:
                print("Não entendi o que foi dito.")
            except sr.RequestError as e:
                print(f"Erro ao conectar com o serviço de reconhecimento de fala: {e}")

StartListen()