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



def functionsKey():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Pronto! Pode falar...")
        playsound('voz.mp3')
        while True:
            audio = recognizer.listen(source)
            
            try:
                speech = recognizer.recognize_google(audio, language="en-US")
                print(f"Você disse em inglês: {speech}")

                commands = {
                    "enter": lambda: pyautogui.press("enter"),
                    "anchor": lambda: pyautogui.press("enter"),
                    "painter": lambda: pyautogui.press("enter"),
                    "space": lambda: pyautogui.press("space"),
                    "up": lambda: pyautogui.press("up"),
                    "down": lambda: pyautogui.press("down"),
                    "left": lambda: pyautogui.press("left"),
                    "right": lambda: pyautogui.press("right"),
                    "esc": lambda: pyautogui.press("esc")
                }

                # Executa a função correspondente ao comando
                command_found = False
                for key in commands:
                    if key in speech.lower():
                        commands[key]()  # Executa o comando correspondente
                        command_found = True
                        StartListen()
                        break

                if not command_found:
                    print(f"Comando não reconhecido: {speech}")

            except sr.UnknownValueError:
                print("Não entendi o que foi dito.")
            except sr.RequestError as e:
                print(f"Erro ao conectar com o serviço de reconhecimento de fala: {e}")




def StartListen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    listening_in_portuguese = False
    with mic as source:
        print("Aguardando a palavra-chave em inglês...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Pronto! Pode falar...")

        while True:
            audio = recognizer.listen(source)
            
            try:
                speech = recognizer.recognize_google(audio, language="en-US")
                print(f"Você disse em inglês: {speech}")

                if "icing" in speech or "I think" in speech or "eye sync" in speech:
                    if "function" in speech:
                       # playsound('voz.mp3')
                        functionsKey()
                    playsound('voz.mp3')
                    switch_to_portuguese()
                    listening_in_portuguese = True 

            except sr.UnknownValueError:
                print("Não entendi o que foi dito.")
            except sr.RequestError as e:
                print(f"Erro ao conectar com o serviço de reconhecimento de fala: {e}")

#StartListen()
