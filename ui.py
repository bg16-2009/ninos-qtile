import os, pyfiglet
from pkgs import opt_pkgs

def banner():
    print(pyfiglet.figlet_format("n i n O S", font="slant"))
    print(pyfiglet.figlet_format("qtile", font="digital"))

def print_text_center(text):
    os.system('setterm -term linux -back blue -fore white -clear')
    rows, columns = os.popen('stty size', 'r').read().split()
    rows = int(rows)
    columns = int(columns)
    result=''
    for i in range(1, rows//2):
        result += '\n'
    result += text.center(columns)
    os.system("clear")
    print(result)

def menu():
    pkgs = []
    for key, pair_list in opt_pkgs.items():
        os.system("clear")
        print('---> ' + key)
        print('\n')
        for index, pair in zip(range(0,len(pair_list)),pair_list):
            print (f'{index+1}. {pair[1]}')
        data=input('Type choices numbers separated by " " (space): ')
        if data != '':
            index_pkgs=data.split()
            for index_pkg in index_pkgs:
                pkgs.append(opt_pkgs[key][int(index_pkg)-1][0])
    os.system("clear")
    return pkgs