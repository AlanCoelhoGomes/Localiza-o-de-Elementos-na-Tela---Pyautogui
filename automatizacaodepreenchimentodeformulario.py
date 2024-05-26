import pyautogui
import time

# Aguarda alguns segundos para posicionar o cursor no primeiro campo do formulário
time.sleep(5)

# Lista com as coordenadas dos campos do formulário
campos_formulario = [(100, 200), (100, 250), (100, 300)]

# Lista com os dados para preencher o formulário
dados_formulario = ['Nome', 'Email', 'Telefone']

# Preenche cada campo do formulário com os dados correspondentes
for campo, dado in zip(campos_formulario, dados_formulario):
    pyautogui.click(campo)
    pyautogui.typewrite(dado)

