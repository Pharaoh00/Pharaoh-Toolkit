import random
import sys
from nomesLista import nomes_list
from nomesLista import sobrenomes_list

def name_Generator():
    print("Gerador de Nomes")
    while(True):
        ask_Opt = input("""
1. Gerar primeiro nome.
2. Gerar sobrenome.
3. Nome + sobrenome.
4. Avançado.
O que deseja fazer?: """)
        if str(ask_Opt) == "-v":
            break
        elif str(ask_Opt) == "exit":
            sys.exit()
        elif ask_Opt.isalpha():
            print("\nSomente as opções a cima\n")
#-----------------------------------------------------------------------------#
        # Primeiro nome
        elif int(ask_Opt) == 1:
            print("Para continuar gerando nomes, ENTER, para sair do programa exit, qualquer tecla para sair")
            while(True):
                print(random.choice(nomes_list))
                ask_User = input("Esse nome está bom?: ")
                if str(ask_User) == "exit":
                    print("Saindo...")
                    sys.exit()
                elif str(ask_User) == "":
                    continue 
                elif str(ask_User) != "exit" or str(ask_User) != "" or ask_User.isdigit():
                    break
#-----------------------------------------------------------------------------#
        # Sobrenome
        elif int(ask_Opt) == 2:
            while(True):
                print(random.choice(sobrenomes_list))
                ask_User = input("Esse nome está bom?: ")
                if str(ask_User) == "exit":
                    print("Saindo...")
                    sys.exit()
                elif str(ask_User) == "":
                    continue 
                elif str(ask_User) != "exit" or str(ask_User) != "" or ask_User.isdigit():
                    break
#-----------------------------------------------------------------------------#
        # Nome + Sobrenome
        elif int(ask_Opt) == 3:
            while(True):
                nome_random = random.choice(nomes_list)
                sobre_random = random.choice(sobrenomes_list)
                print(nome_random, sobre_random)
                ask_User = input("Esse nome está bom?: ")
                if str(ask_User) == "exit":
                    print("Saindo...")
                    sys.exit()
                elif str(ask_User) == "":
                    continue 
                elif str(ask_User) != "exit" or str(ask_User) != "" or ask_User.isdigit():
                    break
#-----------------------------------------------------------------------------#
        # Avançado
        elif int(ask_Opt) == 4:
            try:
                while(True):
                    new_list = []
                    ask_User = str(input("Letra: "))
                    if str(ask_User) == "exit":
                        print("Saindo...")
                        sys.exit()
                    elif str(ask_User) == "-v":
                        break
                    else:
                        for i in range(len(nomes_list)):
                            check = nomes_list[i].startswith(ask_User)
                            if check is True: # is True
                                new_list.append(nomes_list[i]) # Escolhe todos o nomes que começam com a Letra A
                                                               # por exemplo, adiciona eles em new_list 
                                                               # apartir da new_list faz um random.choice para escolher
                        print(random.choice(new_list))
            except IndexError:
                print("Invalido - IndexError. Tente com letras!")

name_Generator()
