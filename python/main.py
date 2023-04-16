import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Agregar nombre al servidor
app.config['NAME'] = 'Servidor 2'


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(message='Pong!')


@app.route('/forward', methods=['GET'])
def forward():
    try:
        url = request.args.get('url')
        server1_response = requests.get('http://localhost:8080/ping')
        # server1_name = server1_response.json().get('serverName')
        response = requests.get(url)
        data = response.json()
        # data['server1Name'] = server1_name
        data['server2Name'] = app.config['NAME']
        return jsonify(data)
    except:
        return jsonify(message='Error executing request'), 500


if __name__ == '__main__':
    app.run(port=4000)
