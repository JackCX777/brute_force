import json
import server_queries
import multiprocessing
import sys
import datetime


def smart_password_attack(target_info_attack, password_list_attack, brute_force_attack, gui_queue=None):
    if gui_queue is not None:
        sys.stderr = sys.stdout
        sys.stdout = gui_queue
    else:
        pass
    with open('attack_settings.json', 'r') as attack_settings_file:
        server_settings_dict = json.load(attack_settings_file)
    brute_force_alphabet = server_settings_dict['brute_force_alphabet']
    password_length = server_settings_dict['password_length']
    target_keyword_list = server_settings_dict['target_keyword_list']
    with open('common_passwords_file.txt', 'r') as password_list_file:
        start_time = datetime.datetime.now()
        if target_info_attack(target_keyword_list,
                              server_queries.request_to_server_json,
                              server_settings_dict
                              ) is not None:
            print('Algorithm type: target info attack')
        elif password_list_attack(password_list_file,
                                server_queries.request_to_server_json,
                                server_settings_dict
                                ) is not None:
            print('Algorithm type: password list attack')
        elif brute_force_attack(brute_force_alphabet,
                          password_length,
                          server_queries.request_to_server_json,
                          server_settings_dict,
                          ) is not None:
            print('Algorithm type: brute force attack')
        else:
            print('Failure of all attacks')
        finish_time = datetime.datetime.now()
        delta_time = finish_time - start_time
        print('Algorithm runtime: ' + str(delta_time))


def password_attack_by_target_info_only(target_info_attack, gui_queue=None):
    if gui_queue is not None:
        sys.stderr = sys.stdout
        sys.stdout = gui_queue
    else:
        pass
    with open('attack_settings.json', 'r') as attack_settings_file:
        server_settings_dict = json.load(attack_settings_file)
    target_keyword_list = server_settings_dict['target_keyword_list']
    start_time = datetime.datetime.now()
    if target_info_attack(target_keyword_list,
                          server_queries.request_to_server_json,
                          server_settings_dict
                          ) is not None:
        print('Algorithm type: target info attack')
    else:
        print('Failure of target info attack')
    finish_time = datetime.datetime.now()
    delta_time = finish_time - start_time
    print('Algorithm runtime: ' + str(delta_time))


def password_attack_by_common_list_only(password_list_attack, gui_queue=None):
    if gui_queue is not None:
        sys.stderr = sys.stdout
        sys.stdout = gui_queue
    else:
        pass
    with open('attack_settings.json', 'r') as attack_settings_file:
        server_settings_dict = json.load(attack_settings_file)
    with open('common_passwords_file.txt', 'r') as password_list_file:
        start_time = datetime.datetime.now()
        if password_list_attack(password_list_file,
                                server_queries.request_to_server_json,
                                server_settings_dict
                                ) is not None:
            print('Algorithm type: password list attack')
        else:
            print('Failure of password list attack')
        finish_time = datetime.datetime.now()
        delta_time = finish_time - start_time
        print('Algorithm runtime: ' + str(delta_time))


def password_attack_by_brute_force_only(brute_force_attack, gui_queue=None):
    if gui_queue is not None:
        sys.stderr = sys.stdout
        sys.stdout = gui_queue
    else:
        pass
    with open('attack_settings.json', 'r') as attack_settings_file:
        server_settings_dict = json.load(attack_settings_file)
    brute_force_alphabet = server_settings_dict['brute_force_alphabet']
    password_length = server_settings_dict['password_length']
    start_time = datetime.datetime.now()
    if brute_force_attack(brute_force_alphabet,
                          password_length,
                          server_queries.request_to_server_json,
                          server_settings_dict,
                          ) is not None:
        print('Algorithm type: brute force attack')
    else:
        print('Failure of brute force attack')
    finish_time = datetime.datetime.now()
    delta_time = finish_time - start_time
    print('Algorithm runtime: ' + str(delta_time))
