from ui import banner, menu
from install_utils import install_esentials, install_from_list, install_configs
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
        time.sleep(1)
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
    print('''
Welcome to ninOS!

Here you can modify your current install!
What do you want to do?
[1] Add more software via a separate menu
[2] Install configs

Type the number with your choice: ''', end='')
    choice=input()
    if(choice=='1'):
        pkg_choices=menu()
        install_from_list(pkg_choices, True)
    elif(choice=='2'):
        install_configs(False)
        print('Configs installed succesfully!')

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
