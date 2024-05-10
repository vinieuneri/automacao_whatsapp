import pyautogui
from time import sleep
import webbrowser
import pyperclip

telefones = []

def escrever_frase(frase):
   pyperclip.copy(frase)
   pyautogui.hotkey('ctrl','v')

with open('fones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    iniciar_conversa = pyautogui.locateCenterOnScreen('btn_iniciar.png')
    pyautogui.moveTo(iniciar_conversa[0],iniciar_conversa[1], duration=1)
    pyautogui.click()
    sleep(2)
    abrir_whats = pyautogui.locateCenterOnScreen('abrir_whatsapp.png')
    pyautogui.moveTo(abrir_whats[0],abrir_whats[1], duration=1)
    pyautogui.click()
    sleep(3)
    pyautogui.click(564,805, duration=2)
    escrever_frase('Teste de automação, favor ignorar!')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)

