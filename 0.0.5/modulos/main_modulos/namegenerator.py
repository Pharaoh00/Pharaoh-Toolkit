import random
from ..listas import *

class NameGeneretor:

    is_done = False
    new_name_list = []

    def __init__(self):
        self.print_nomes()

    def print_nomes(self):
        while not self.is_done:
            self.ask_opt = input("""
a. Gerar primeiro nome.
b. Gerar sobrenome.
c. Nome + sobrenome.
d. Avançado.
O que deseja fazer?: """)
            if str(self.ask_opt) == "exit":
                print("Saindo...")
                self.is_done = True
            elif str(self.ask_opt) == "-v":
                print("Voltando...")
                break
            elif self.ask_opt.isdigit():
                print(self.ask_opt, "- Não é valido. Tente as opções a cima")
            elif(str(self.ask_opt) != "a" and
                 str(self.ask_opt) != "b" and
                 str(self.ask_opt) != "c" and
                 str(self.ask_opt) != "d"):
                print(self.ask_opt, "- Não é valido. Tente as opções a cima")
            elif str(self.ask_opt) == "a":
                self.check_opt(nomesLista_First.nomes_list)
            elif str(self.ask_opt) == "b":
                self.check_opt(nomesLista_Second.sobrenomes_list)
            elif str(self.ask_opt) == "c":
                self.check_opt(nomesLista_First.nomes_list, 
                               nomesLista_Second.sobrenomes_list)
#-----------------------------------------------------------------------------#
    def check_opt(self, check_list_x, check_list_y=None):
        while not self.is_done:
            self.print_rlg = self.random_nomes(check_list_x, check_list_y)
            print(self.print_rlg)
            self.ask_opt_continue = input("Esse nome está bom?: ")
            if str(self.ask_opt_continue) == "":
                continue
            elif str(self.ask_opt_continue) == "exit":
                print("Saindo...")
                self.is_done = True
            elif str(self.ask_opt_continue) == "-v":
                break
#-----------------------------------------------------------------------------#
    def random_nomes(self, rlg_x, rlg_y): # rlg = Random List Generetor
        self.rlg_x = rlg_x
        self.rlg_y = rlg_y

        if self.rlg_y is None:
            return random.choice(self.rlg_x)                    
        elif self.rlg_y is not None:
            self.rlg_x = random.choice(rlg_x)
            self.rlg_y = random.choice(rlg_y)
            return self.rlg_x + " " + self.rlg_y

    #def primeiro_nomes(self, list_primeiro):
    #    self.list_primeiro = random.choice(list_primeiro)
    #    return self.list_primeiro

    #def sobrenome_nomes(self, list_sobrenome):
    #    self.list_sobrenome = random.choice(list_sobrenome)
    #    return self.list_sobrenome

    #def primeiro_sobrenome_nomes(self, list_x, list_y):
    #    self.list_x = random.choice(list_x)
    #    self.list_y = random.choice(list_y)
    #    return self.list_x + " " + self.list_y
#-----------------------------------------------------------------------------#
    # Trabalhar melhor, tentar inserir o "avançado" nas opções normais
    def avancado_nomes(self, avanc_list):
        self.avanc_list = avanc_list
        self.test_opt = input("Letra: ")
        for i in range(len(self.avanc_list)):
            self.avanc_list = nomes_list[i].startswith(self.test_opt)
            if self.avanc_list is True: # is True
                self.new_name_list.append(self.avanc_list[i])

        return random.choice(self.new_name_list)


#NG = NameGeneretor()
