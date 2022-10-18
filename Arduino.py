from pyfirmata import Arduino
import time
import requests
from flask import Flask

app = Flask(__name__)


@app.route('/health')
def healthCheck():
    return {'status': 'ok'}


app.run(host='0.0.0.0')

if __name__ == '__main__':
    Uno = Arduino('COM3')

    nome_semaforo = 'SPZS32'

    url = 'http://localhost:8080/semaforo'

    urlNovosTempos = 'http://localhost:8080/tempoSemaforo/'

    headers = {'Content-type': 'application/json'}

    json_request = {'identificador': 'primeiroTeste', 'identificadorSemaforoPrincipal': '', 'tempoInverso': False}

    retorno_api = requests.post(url, json=json_request, headers=headers)

    novos_tempos = retorno_api.json()

    while True:
        Uno.digital[11].write(0)  # Vermelho semáforo 1

        Uno.digital[13].write(1)  # Verde semáforo 1

        time.sleep(novos_tempos['tempoVerde'])

        Uno.digital[13].write(0)  # Verde semáforo 1

        Uno.digital[12].write(1)  # Amarelo semáforo 1

        time.sleep(novos_tempos['tempoAmarelo'])

        Uno.digital[12].write(0)  # Amarelo semáforo 1

        Uno.digital[11].write(1)  # Vermelho semáforo 1

        time.sleep(novos_tempos['tempoVermelho'])

        if requests.get('http://localhost:8080/camera'):
            novos_tempos = requests.get(urlNovosTempos + nome_semaforo)
