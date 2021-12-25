from ui import banner, menu
from install_utils import install_esentials, install_from_list
import os, time

def install():
    print('''
Welcome to ninOS installer!

Do you want to install extra packages via a separate menu? [Y/n] ''', end='')
    opt=input()
    opt_pkg_choice=[]
    if(opt.lower()=='y'):
        os.system("clear")
        print("Opening menu....")
        time.delay(1)
        opt_pkg_choice=menu()
    os.system("clear")
    print('Installing ninOS.....')
    v = input('Do you want details about the install? [Y/n] ')
    if(v.lower()=='y'):
        v=True
    elif(v.lower()=='n'):
        v=False
    install_esentials(v)
    install_from_list(opt_pkg_choice, v)
    install_configs(v)
    os.system('sudo systemctl enable NetworkManager')
    os.system('sudo systemctl enable sddm')
    os.system("clear")
    print('Install complete!')
    print('You now have ninOS in your system!')
    print('You should reboot your compuer!')

def modify():
    print('Work in progress!')


def main():
    banner()
    print(f'''
[1] Install ninOS
[2] Modify your current system

Select your option: ''', end='')
    choice=int(input())
    if choice==1:
        os.system("clear")
        install()
    elif choice==2:
        os.system("clear")
        modify()

main()
