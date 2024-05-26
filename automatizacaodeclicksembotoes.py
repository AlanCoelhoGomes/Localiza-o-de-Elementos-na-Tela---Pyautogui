import pyautogui
import time

# Aguarda alguns segundos para posicionar o cursor onde deseja clicar
time.sleep(5)

# Localiza o botão na tela e obtém suas coordenadas
botao_x, botao_y = pyautogui.locateCenterOnScreen('botao.png')

# Move o cursor para as coordenadas do botão e clica
pyautogui.moveTo(botao_x, botao_y)
pyautogui.click()

