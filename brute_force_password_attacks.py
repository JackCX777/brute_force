# This module contains simple brute force password algorithms.


def brute_force_password(alphabet, length, query, query_settings_dict, iter_number=0):
    """
        This function provides simple brute force algorithm for password phrase.

        Parameters:
            alphabet (str): A character set for the search in many variations.
            length (int) : Minimal length of password phrase
            query (func) : Function, that request to server.
            query_settings_dict (dict) : Dictionary with current settings.
            iter_number (int) : Number of iteration in cycle.

        Returns:
            password_brute_force (str) : Password phrase if success.
    """
    server_login = query_settings_dict['server_login']
    net_protocol = query_settings_dict['net_protocol']
    net_node = query_settings_dict['net_node']
    net_port = query_settings_dict['net_port']
    net_path = query_settings_dict['net_path']
    # Let alphabet is a number in the calculation system with a basis equal to the length of alphabet.
    alphabet_base = len(alphabet)
    attempt_number = 0
    # Then in the cycle we will translate each next number from the decimal system
    # into a system with a base equal to the length of the alphabet.
    # temp - a temporary variable to keep the current value of iter_number.
    # The internal cycle works until the number that is obtained by an integer division turns into 0.
    # rest - the remainder of the division,
    # which must be inserted at the beginning to obtain a number in the calculation system with alphabet_base basis.
    # Because rest is a number in the decimal system, we take the symbol that corresponds to it in alphabet instead.
    # password_brute_force is a variable that contains the current number obtained in the calculation system
    # with alphabet_base as the basis.
    # length - the length of the password value in the current iteration of the cycle
    # to substitute leading zeros if password_brute_force length < length.
    # Print the number of the current attempt, the current length and the current password_brute_force value.
    while True:
        attempt_number += 1
        temp = iter_number
        password_brute_force = ''
        while temp != 0:
            rest = temp % alphabet_base
            temp = temp // alphabet_base
            # while len(password_brute_force) < length:
            #     password_brute_force = '0' + password_brute_force
            password_brute_force = alphabet[rest] + password_brute_force  # Equal two lines above.
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
        # Here we take the last symbol from alphabet.
        if alphabet[-1] * length == password_brute_force:
            length += 1
            iter_number = 0
        else:
            iter_number += 1
