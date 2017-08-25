# main.py
# ToolKit criado por Pharaoh
# Versão 0.0.5 (2017) [Sex, 25 Ago 09:10:21]
# Linguagem = PT-BR

# Novo na versão 0.0.5:
# Atualização para Objeto Orientado.
# Adicionado modulo Gerador de Nomes
# Adicionado Menu "mutavel". 
#
#-----------------------------------------------------------------------------#
# Objeto Orientado:
# Modulo Gerador de senha foi convertido para OOP.
# Nova classe criada, PasswordGenerator.
# Novas funções criadas, pass_print, pass_all, pass_custom.
# Otimização do codigo, mais "enxuto" e mais simples de compreender.
#
# Modulo Calculadora foi convertido para OOP
# Nova classe criada, Calculadora
# Novas funcções criadas, calc_print, calc_mmc, calc_fib, calc_prime
#-----------------------------------------------------------------------------#

import time
import sys
import sysconfig
#from . import passwordgeneretor
#try:
#    from . import calculadora
#except:
#    pass
#    print("Modulo calculadora não foi encontrado")
from .main_modulos import *

def main():
    # Itens do MENU
    menu = ["a. ~~Gerador de senha~", 
            "b. ~~Calculadora~~", 
            "c. ~~Gerador de Nomes~~"]
    # ANIMÇÃO DO INICIO DO PROGRAMA
    print("""""")
    time.sleep(0.1)
    print("   /$$$$$$$$                  /$$ /$$   /$$ /$$   /$$     ")
    time.sleep(0.1)
    print("  |__  $$__/                 | $$| $$  /$$/|__/  | $$     ")
    time.sleep(0.1)
    print("     | $$  /$$$$$$   /$$$$$$ | $$| $$ /$$/  /$$ /$$$$$$   ")
    time.sleep(0.1)
    print("     | $$ /$$__  $$ /$$__  $$| $$| $$$$$/  | $$|_  $$_/   ")
    time.sleep(0.1)
    print("     | $$| $$  \ $$| $$  \ $$| $$| $$  $$  | $$  | $$     ")
    time.sleep(0.1)
    print("     | $$| $$  | $$| $$  | $$| $$| $$\  $$ | $$  | $$ /$$ ")
    time.sleep(0.1)
    print("     | $$|  $$$$$$/|  $$$$$$/| $$| $$ \  $$| $$  |  $$$$/ ")
    time.sleep(0.1)
    print("     |__/ \______/  \______/ |__/|__/  \__/|__/   \___/   ")
    print("")
    time.sleep(0.1)
    print("")
    print("")
    time.sleep(0.1)
    print("  @@@@@@@   @@@  @@@   @@@@@@   @@@@@@@    @@@@@@    @@@@@@   @@@  @@@  ")
    time.sleep(0.1)
    print("  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  ")
    time.sleep(0.1)
    print("  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  ")
    time.sleep(0.1)
    print("  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  ")
    time.sleep(0.1)
    print("  @!@@!@!   @!@!@!@!  @!@!@!@!  @!@!!@!   @!@!@!@!  @!@  !@!  @!@!@!@!  ")
    time.sleep(0.1)
    print("  !!@!!!    !!!@!!!!  !!!@!!!!  !!@!@!    !!!@!!!!  !@!  !!!  !!!@!!!!  ")
    time.sleep(0.1)
    print("  !!:       !!:  !!!  !!:  !!!  !!: :!!   !!:  !!!  !!:  !!!  !!:  !!!  ")
    time.sleep(0.1)
    print("  :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  ")
    time.sleep(0.1)
    print("   ::       ::   :::  ::   :::  ::   :::  ::   :::  ::::: ::  ::   :::  ")
    time.sleep(0.1)
    print("   :         :   : :   :   : :   :   : :   :   : :   : :  :    :   : :  ")
    time.sleep(0.1)
    print("""""")
    #
    # Para ajuda -help.
    print("""Para mais informações -help""")
    while(True):
        # MENU.
        print("""___  ___ _____ _   _ _   _ 
|  \/  ||  ___| \ | | | | |
| .  . || |__ |  \| | | | |
| |\/| ||  __|| . ` | | | |
| |  | || |___| |\  | |_| |
\_|  |_/\____/\_| \_/\___/ 
""")#---#
        for i in menu:
            print(i)
        ask_user_main = input("O que deseja fazer? ")
        if ask_user_main.isdigit():
            print(ask_user_main, """- Não é valido. Tente as opções a cima.""")
        # -help.
        elif str(ask_user_main) == "-help":
            pass
        # Para sair do programa.
        elif str(ask_user_main) == "exit":
            print("Saindo...")
            time.sleep(0.2)
            sys.exit()
        elif str(ask_user_main) == "python":
            print("")
            print("Você está rodando python na versão:", sys.version)
            print("Você está rodando:",sysconfig.get_platform())
            print("")
        # Modulo Gerador de Senha.
        if str(ask_user_main) == "a":
            passwordgeneretor.PasswordGenerator()
        # Modulo Calculadora.
        elif str(ask_user_main) == "b":
            calculadora.Calculadora()
        # Modulo Gerador de Nomes.
        elif str(ask_user_main) == "c":
            namegenerator.NameGeneretor()
















