import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

app.config['NAME'] = 'Servidor 2'


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(message='Pong!')


@app.route('/forward', methods=['GET'])
def forward():
    try:
        url = request.args.get('url')
        response = requests.get(url)
        data = response.json()
        data['server2Name'] = app.config['NAME']
        return jsonify(data)
    except:
        return jsonify(message='Error executing request'), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
