import pyautogui
import time

# Aguarda alguns segundos para posicionar o cursor no ponto inicial
time.sleep(5)

# Localiza o objeto que será arrastado na tela
objeto_x, objeto_y = pyautogui.locateCenterOnScreen('objeto.png')

# Move o cursor para o objeto e clica para começar o arrastar
pyautogui.moveTo(objeto_x, objeto_y)
pyautogui.mouseDown()

# Move o cursor para o ponto final e solta o objeto
pyautogui.moveTo(500, 500)
pyautogui.mouseUp()

