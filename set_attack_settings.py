# This module sets the attack settings.


import json


server_login = 'cat'  # Target login
password_length = 0  # The minimum length from which the search begins
net_protocol = 'http'  # Server protocol
net_node = '127.0.0.1'  # Server address
net_port = '5000'  # Server port
net_path = 'auth'  # Server authorisation page path
net_query = '???'  # The format of authorization on the server. Only json has been implemented. Not used.
brute_force_alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'  # Alphabet fore brute force search.
password_top = 100  # The number of top first passwords to be taken from the dictionary of common passwords.


with open('target_info.txt', 'r') as target_info_file:
    """
    Opens target_info.txt file and sets target info dictionary for attack.
    """
    target_info_list = target_info_file.read().strip().split('\n')
# print(target_info_list)


with open('common_passwords_file.txt', 'r') as password_list_file:
    """
    Opens common_passwords_file.txt file and gets the top part for smart attack.
    """
    top_common_passwords_list = []
    for place in range(password_top):
        common_password = password_list_file.readline().strip()
        top_common_passwords_list.append(common_password)
# print(top_common_passwords_list)


target_smat_keyword_list = target_info_list + top_common_passwords_list
"""
Generates the attack dictionary of keywords from the target_info.txt file 
and the top part of the common_passwords_file.txt file.
"""
# print(target_smat_keyword_list)


"""
Configure the attack settings with attack_settings.json file.
"""
server_settings_dict = {
        'server_login': server_login,
        'password_length': password_length,
        'net_protocol': net_protocol,
        'net_node': net_node,
        'net_port': net_port,
        'net_path': net_path,
        'net_query': net_query,
        # 'net_address': net_address,
        'brute_force_alphabet': brute_force_alphabet,
        'target_keyword_list': target_smat_keyword_list
    }
with open('attack_settings.json', 'w') as attack_settings_file:
    json.dump(server_settings_dict, attack_settings_file, indent=4, sort_keys=False)
