from pyfirmata import Arduino, util
import time
import requests
import json

if __name__ == '__main__':
    Uno = Arduino('COM3')

    url = 'http://localhost:8080/semaforo'

    headers = {'Content-type': 'application/json'}

    jsonRequest = {'identificador':'primeiroTeste', 'identificadorSemaforoPrincipal':'', 'tempoInverso': False}

    retornoApi = requests.post(url, json = jsonRequest, headers = headers)

    novosTempos = retornoApi.json()

    while True:
        Uno.digital[11].write(0)    # Vermelho semáforo 1
        Uno.digital[13].write(1)    # Verde semáforo 1
        time.sleep(novosTempos['tempoVerde'])
        Uno.digital[13].write(0)    # Verde semáforo 1
        Uno.digital[12].write(1)    # Amarelo semáforo 1
        time.sleep(novosTempos['tempoAmarelo'])
        Uno.digital[12].write(0)    # Amarelo semáforo 1
        Uno.digital[11].write(1)    # Vermelho semáforo 1
        time.sleep(novosTempos['tempoVermelho'])