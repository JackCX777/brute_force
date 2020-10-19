import json


server_login = 'jack'
password_length = 0
net_protocol = 'http'
net_node = '127.0.0.1'
net_port = '5000'
net_path = 'auth'
net_query = '???'
net_address = 'http://127.0.0.1:5000/auth'
brute_force_alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
password_top = 100

with open('target_info.txt', 'r') as target_info_file:
    target_info_list = target_info_file.read().strip().split('\n')
# print(target_info_list)

with open('common_passwords_file.txt', 'r') as password_list_file:
    top_common_passwords_list = []
    for place in range(password_top):
        common_password = password_list_file.readline().strip()
        top_common_passwords_list.append(common_password)
# print(top_common_passwords_list)

target_smat_keyword_list = target_info_list + top_common_passwords_list
# print(target_smat_keyword_list)

server_settings_dict = {
        'server_login': server_login,
        'password_length': password_length,
        'net_protocol': net_protocol,
        'net_node': net_node,
        'net_port': net_port,
        'net_path': net_path,
        'net_query': net_query,
        'net_address': net_address,
        'brute_force_alphabet': brute_force_alphabet,
        'target_keyword_list': target_smat_keyword_list
    }
with open('attack_settings.json', 'w') as attack_settings_file:
    json.dump(server_settings_dict, attack_settings_file, indent=4, sort_keys=False)
