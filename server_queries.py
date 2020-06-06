import requests


def request_to_server_json(protocol, node, port, path, login_word, password_phrase):
    response = requests.post(f'{protocol}://{node}:{port}/{path}',
                             json={'login': login_word, 'password': password_phrase})
    return response.status_code
    # return response.status_code == 200
    # if response.status_code == 200:
    #     print()
    #     print('Success! Target has been hacked!')
    #     print(f'Target login: {login}   Target password: {password}')
    #     return True
    # else:
    #     print(f'Status code: {response.status_code}')
    #     return False
