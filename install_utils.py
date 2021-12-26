from pkgs import pkgs_esential
import os, shutil

def install_pkg(pkg, v):
    if(v==True):
        print(f'Installing {pkg}....')
    os.popen(f'nohup sudo pacman -S {pkg} --noconfirm > ninos.log').read()

def install_from_list(pkgs, v):
    for pkg in pkgs:
        install_pkg(pkg, v)

def install_esentials(v):
    install_from_list(pkgs_esential, v)

def install_configs(v):
    home=os.popen('echo $HOME').read()
    
    if(v==True):
        print(f'Installing special configs in the {home} directory')
        print('(If something goes wrong you can reinstall them from the modify menu)')
    os.system(f'mkdir {home}/.config/alacritty')
    shutil.copy(
        f'{os.getcwd()}/configs/alacritty/alacritty.yml', 
        f'{home}/.config/alacritty/'
    )
    shutil.copy(
        f'{os.getcwd()}/configs/.Xauthority', 
        f'{home}/'
    )
    shutil.copy(
        f'{os.getcwd()}/configs/config.py', 
        f'{home}/.config/qtile/'
    )
    