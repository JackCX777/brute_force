# This is the main file for run program by console.
# You should run test_server_WSGI.py file before run this script
# to start local test server on http://127.0.0.1:5000.
# Attack type selection provides by enter character equal chosen command.
# If You like, You can edit set_attack_settings.py and target_info.txt files
# for reconfigure attack dictionaries such as target information, common passwords and other.


import substitution_password_attacks
import brute_force_password_attacks
import attack_plans


while True:
    command = input('\n'
                    '\n'
                    'Note that you should run test_server_WSGI.py before start the attack!!!\n'
                    'Type s for set attack settings.\n'
                    'Type 1 for smart attack.\n'
                    'Type 2 for attack by target info dictionary.\n'
                    'Type 3 for attack by common passwords dictionary.\n'
                    'Type 4 fore simple brute force attack.\n'
                    'Type 0 for exit.\n'
                    'Your command: ').strip()
    if command == '0':
        break
    elif command == 's':
        import set_attack_settings
    elif command == '1':
        """
        This line provides smart password attack algorithm, 
        that runs attack by target keyword dictionary(contains keywords from target info 
        and top part of common passwords) at first, 
        attack by top of the common passwords from dictionary at second, 
        and simple brute force attack if other fails. 
        """
        attack_plans.smart_password_attack(
            substitution_password_attacks.brute_by_target_info,
            substitution_password_attacks.brute_by_password_list,
            brute_force_password_attacks.brute_force_password
        )
    elif command == '2':
        """
        This line provides password attack by target info dictionary algorithm.
        """
        attack_plans.password_attack_by_target_info_only(substitution_password_attacks.brute_by_target_info)
    elif command == '3':
        """
        This line provides password attack by common passwords dictionary algorithm.
        """
        attack_plans.password_attack_by_common_list_only(substitution_password_attacks.brute_by_password_list)
    elif command == '4':
        """
        This line provides password attack by simple brute force algorithm.
        """
        attack_plans.password_attack_by_brute_force_only(brute_force_password_attacks.brute_force_password)
    else:
        print('Wrong command! Try again!')
