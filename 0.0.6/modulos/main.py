# main.py
# ToolKit criado por Pharaoh
# Versão 0.0.6 (2018) [Sex, 14 Set 10:01:35]
# Linguagem = PT-BR

# Novo na versão 0.0.6:
#
# Modulo de formatar strings criado. Nome: prototypeformat.py
# main.py agora usa, como teste, o modulo formatar(centralizado) nas
# opções do menu, menu ASCII, e opções do menu.
# Agora, user_input, utiliza o modulo de formatar(com a data atual e hora),
# simplificando o codigo geral.

import time
import sys
import sysconfig
#from . import passwordgeneretor
#try:
#    from . import calculadora
#except:
#    pass
#    print("Modulo calculadora não foi encontrado")
from .MainModulos import *
formating = prototypeformat.FormatString()

def main():
    # Itens do MENU
    menu = ["a. ~~Gerador de senha~", 
            "b. ~~Calculadora~~", 
            "c. ~~Gerador de Nomes~~"]
    # ANIMÇÃO DO INICIO DO PROGRAMA
    intro = ["   /$$$$$$$$                  /$$ /$$   /$$ /$$   /$$     ",
             "  |__  $$__/                 | $$| $$  /$$/|__/  | $$     ",
             "     | $$  /$$$$$$   /$$$$$$ | $$| $$ /$$/  /$$ /$$$$$$   ",
             "     | $$ /$$__  $$ /$$__  $$| $$| $$$$$/  | $$|_  $$_/   ",
             "     | $$| $$  \ $$| $$  \ $$| $$| $$  $$  | $$  | $$     ",
             "     | $$| $$  | $$| $$  | $$| $$| $$\  $$ | $$  | $$ /$$ ",
             "     | $$|  $$$$$$/|  $$$$$$/| $$| $$ \  $$| $$  |  $$$$/ ",
             "     |__/ \______/  \______/ |__/|__/  \__/|__/   \___/   ",
             "",
             "",
             "  @@@@@@@   @@@  @@@   @@@@@@   @@@@@@@    @@@@@@    @@@@@@   @@@  @@@  ",
             "  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  ",
             "  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  ",
             "  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  ",
             "  @!@@!@!   @!@!@!@!  @!@!@!@!  @!@!!@!   @!@!@!@!  @!@  !@!  @!@!@!@!  ",
             "  !!@!!!    !!!@!!!!  !!!@!!!!  !!@!@!    !!!@!!!!  !@!  !!!  !!!@!!!!  ",
             "  !!:       !!:  !!!  !!:  !!!  !!: :!!   !!:  !!!  !!:  !!!  !!:  !!!  ",
             "  :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  ",
             "   ::       ::   :::  ::   :::  ::   :::  ::   :::  ::::: ::  ::   :::  ",
             "   :         :   : :   :   : :   :   : :   :   : :   : :  :    :   : :  ",
             "",
             ""]
    #
    # Para ajuda -help.
    for i in intro:
        #print(i)
        print(formating.formatCenter(i, "CENTER"), end="")
    print(formating.formatCenter("Para mais informações -help", "CENTER"))
    while(True):
        # MENU.
        menu_ascii = ["___  ___ _____ _   _ _   _",
                      " |  \/  ||  ___| \ | | | | |",
                      " | .  . || |__ |  \| | | | |",
                      " | |\/| ||  __|| . ` | | | |",
                      " | |  | || |___| |\  | |_| |",
                      " \_|  |_/\____/\_| \_/\___/ "]
        
        for i in menu_ascii:
            print(formating.formatCenter(i, "CENTER"), end="")
        #print("\n")
        print(formating.formatCenter("#----------------------------------#",
                                     "CENTER"), end="")
        for i in menu:
            print(formating.formatCenter(i, "CENTER"), end="")
            print(formating.formatCenter("#----------------------------------#",
                                         "CENTER"), end="")
        print("\n")
        ask_user_main = input(formating.formatDate("O que deseja fazer? "))
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
















