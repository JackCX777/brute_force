# This is a simple test server program, that run local http server on http://127.0.0.1:5000 asynchronously.
# Now in development!!!!! Doesn't work!!!!!!!


import json
from quart_trio import QuartTrio, request, response
from functools import partial
import trio
from hypercorn.trio import serve
from hypercorn.config import Config

app = QuartTrio(__name__)
config = Config()
config.bind = ['localhost:5000']

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
    return response(status=status_code)


async def start_app(task_status=trio.TASK_STATUS_IGNORED):
    # part_app = partial(serve, app, config)
    await serve(app, config)
    trio.from_thread.run(DDDD.main)
    # return part_app

trio.run(start_app)

if __name__ == '__main__':
    # http_server = WSGIServer(('', 5000), app.run())
    # http_server.serve_forever()
    # app.run()
    trio.run(start_app)
