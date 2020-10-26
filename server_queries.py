# This module contains request_to_server_json() function that provides put request with given parameters
# to the server.


import requests


def request_to_server_json(protocol, node, port, path, login_word, password_phrase):
    """
        This function provides put request to the server with given parameters
        and returns server status code response.

        Parameters:
            protocol (str): This string variable contains server protocol, http or https e.g.
            node (str) : Domain or IP server address.
            port (str) : Port, that use target server, 5000 for test server e.g.
            path (str) : Path to servers authorisation page, auth for test server e.g.
            login_word (str) : Target login on target server.
            password_phrase (str) : Current character set for matching with password phrase of target login.

        Returns:
            response.status_code (int) : Status code of the servers response.
    """
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
