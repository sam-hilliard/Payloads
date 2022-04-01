import platform
import socket as s
import requests
import getpass
import os


def main():
    info = general_info()
    
    [local_ip, global_ip] = get_ip()
    info += f'Local IP: {local_ip}\n'
    info += f'Global IP: {global_ip}\n'

    info += f'Current User: {getpass.getuser()}\n'

    info += f'CWD: {os.getcwd()}\n'

    print(info)


def general_info():
    sys = platform.uname()

    info = f'OS: {sys.system}\n'
    info += f'Machine Name: {sys.node}\n'
    info += f'Version: {sys.version}\n'
    info += f'Architect Type: {sys.machine}\n'
    info += f'Processor: {sys.processor}\n'

    return info

def get_ip():
    host_name = s.gethostname()
    local_ip = s.gethostbyname(host_name)
    global_ip = requests.get('https://api.ipify.org').text


    return local_ip, global_ip


if __name__ == '__main__':
    main()