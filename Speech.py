import pyperclip as pc
import speech_recognition as sr
import pyautogui
#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
#Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
    #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
    #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
    #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)
    try:
    #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio,language='pt-BR')
    #Após alguns segundos, retorna a frase falada
        print("Você disse: " + frase)
        pc.copy(frase)
        pyautogui.hotkey('ctrl', 'v')
      #  pyautogui.press('enter')
    #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.UnkownValueError:
        print("Não entendi")
    return frase
ouvir_microfone()
