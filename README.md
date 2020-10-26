# Brute force program.  

This is a toy program, written in pure Python for the learning purposes only
(thanks God).
Caution! It's strictly forbidden to use or reuse this code or its algorithms
or the entire program partly or fully for any legal or illegal attempts to 
get somebody's information, such as passwords, logins, personal data or 
anything else! The public / commercial playback or broadcast of the 
multimedia used in this program is prohibited as well. The commercial use of 
the code is also not permitted, you know.
The program must be used only with local test server.
This application provides several algorithms of brute-force password 
recovery for known login on the server. 
Please note, that project now is on the developing stage.

# Install

Download the application files by link and extract if needed:
https://github.com/JackCX777/brute_force/archive/master.zip
If you have brute_force_GUI_portable file only, just run it and enjoy.
In other cases, you will have to perform some preparations:
Download and install Python 3.8 or above as recommended on official 
Python's website https://www.python.org
Open terminal window from applications folder and install program 
requirements by following commands:
$ cd venv/bin/
$ pip install -r requirements.txt
Application tested on macOS Catalina 10.15.6 and 
Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27).

# Program usage

You can use this program in GUI or in terminal mode.

If you prefer GUI mode:
Run the brute_force_GUI or brute_force_GUI_portable file required to your 
operation system.
Interface description:
Protocol - protocol used by target server, http or https e.g.
Node - servers network address, yandex.ru e.g. 
Port - servers port, 5000 e.g.
Path - path to authorisation page on target server without /, 
auth e.g.
Auth format radiobuttons provide selection of authorisation 
format on the target server, json or headers e.g. Json only
works now.
Run test server button - launches simple test server on localhosts 5000 port, 
automatically fills all server address fields and auth format, then disables 
its editing. You can open your browser and go to the test servers home page 
on http://127.0.0.1:5000 address. On this page you can see the number of 
attempts to login on the server and the number of success authorisations on 
the server.
Stop test server button - stops the test server and restores the ability to
edit all target servers fields and radiobuttons.
Target login field - the username or e-mail should be specified here depending on the authorisation rules on the target 
server. There are three users on the test server: admin, cat and jack.
Min password length field - if you have some information about passwords 
length (servers requirement for a minimum password length is six characters
or you know that the user has a password consisting of three symbols e.g.),
you can reduce the working time of simple brute force algorithm by 
specifying here a number that corresponds to the minimum length of the 
password.Then the program will start brute force from given length and skip 
all passwords that are shorter (but an empty password will be included). 
This option works only when Attack method set to Brute force attack.
Attack method radiobuttons - before starting the attack, you can choose the 
password search algorithm from three options:
Smart attack - attack by target info will start first, that 
substitutes each word from target_info.txt file and top of the 
common_passwords_file.txt (top 100 by default) as a password, then goes 
through combinations of any two;
starts attack by common passwords will be started at second, that 
substitutes words from common_passwords_file.txt file one by one;
simple brute force attack will be started at the end, if all previous fails, 
that substitutes characters from given alphabet in any possible 
combinations.
Dictionary attack - attack by common passwords only will be lanched.
Brute force attack - simple brute force attack only will be lanched.
Start attack button - checks all attack options and starts the selected 
attack, if correct. In addition start multimedia (audio) playback in 
infinity loop while attack is in progress.
Stop attack button - stops all current attacks if any and stops multimedia 
playback.
Progressbar - shows any attack that is in progress now.
Text screen – creates program feedback in text format.
 
If you prefer terminal mode:
Change the attack settings by editing set_attack_settings.py file if you 
like.
Open the terminal from applications folder.
Run the test server by console command:
$ python3 test_server_WSGI.py
Run the application by console command:
$ python3 main.py 
Type s for set attack settings if you have changed the 
set_attack_settings.py file.
Type 1 for smart attack.
Type 2 for attack by target info dictionary only.
Type 3 for attack by common passwords dictionary only.
Type 4 fore simple brute force attack only.
Type 0 for exit.
All attack descriptions are given above.

# Additional info

You can edit attack_settings.json, common_passwords_file.txt, 
set_attack_settings.py and target_info.txt files if you want to change the 
settings of the attack such as target login, list of common passwords, top
number of common passwords, list of target info etc.
