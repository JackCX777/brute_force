# -*- coding: utf-8 -*-

# This is a simple test server program, that run local http server on http://127.0.0.1:5000 synchronously.
# If You like to run it using WSGI from gevent library, edit start_app() function
# or just use default flask services(recommended).


import json
from flask import Flask, request, Response
# from gevent.pywsgi import WSGIServer
import os
import sys


app = Flask(__name__)

stats = {
    'attempts': 0,
    'success': 0,
}


@app.route('/')
def hello():
    return f'This is a test server! Stats={stats}'


@app.route('/auth', methods=['POST'])
def auth():
    stats['attempts'] += 1

    data = request.json
    login = data['login']
    password = data['password']

    with open('test_server_users.json') as users_file:
        users = json.load(users_file)

    # users_file = open('test_server_users.json')
    # users = json.load(users_file)
    # users_file.close()

    if login in users and users[login] == password:
        status_code = 200
        stats['success'] += 1
    else:
        status_code = 401

    return Response(status=status_code)


def start_app():
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
    app.run()


stdout_devnul = open(os.devnull, 'w')
sys.stderr = stdout_devnul
sys.stdout = stdout_devnul

if __name__ == '__main__':
    # app.run()
    start_app()
