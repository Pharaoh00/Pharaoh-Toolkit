import string
import random
import sys
#-----------------------------------------------------------------------------#
# OOP Gerador de Password
class PasswordGenerator:

    s_lower = string.ascii_lowercase
    s_upper = string.ascii_uppercase
    s_letter = string.ascii_letters
    s_digits = string.digits
    s_punctuation = string.punctuation
    is_done = False

    def __init__(self):
        self.pass_print()

    def pass_print(self):
        while not self.is_done:
            self.ask_user = input("""
Gerador de Password
As opções são:
a. Normal
b. Avançado
>> """)#----#
            if str(self.ask_user) == "exit":
                print("Saindo...")
                sys.exit() # Sai completamente
            elif str(self.ask_user) == "-v":
                print("Voltando...")
                self.is_done = True # Quebra o loop atual
            # -- Não esqucer de adicionar as opções -- #
            elif self.ask_user.isdigit(): # Caso numero
                print(self.ask_user, "- Não é valido. Tente as opções a cima")
            elif str(self.ask_user) != "a" and str(self.ask_user) != "b":
                print(self.ask_user, "- Não é valido. Tente as opções a cima")
#-----------------------------------------------------------------------------#
            # NÃO ESQUECER DE COLOCAR AS OPÇÕES A E B DENTRO DE UM WHILE
            # PARA NAO VOLTAR DIRETO PARA O MENU PRINCIPAL
            # Caso "Normal"
            elif str(self.ask_user) == "a":
                while(True):
                    self.ask_user_type = input("""
Opção MENU:
fraca
media
forte
insana
>> """)#------------#
                    if str(self.ask_user_type) == "exit":
                        print("Saindo...")
                        sys.exit()
                    elif str(self.ask_user_type) == "-v":
                        print("Voltando...")
                        break
                    elif self.ask_user_type.isdigit():
                        print(self.ask_user_type,
                              "- Não é valido. Somente as opções a cima!")
                    elif (str(self.ask_user_type) != "fraca" and 
                          str(self.ask_user_type) != "media" and 
                          str(self.ask_user_type) != "forte" and 
                          str(self.ask_user_type) != "insana"):
                        print(self.ask_user_type, "- Não é valido.")
                    else:
                        self.ask_user_number = input("Numero: ") # self.ask_number
                        if self.ask_user_number.isalpha():
                            print(self.ask_user_number, "- Não é valido")
                        else:
                            self.pass_all(self.ask_user_type, 
                                  self.ask_user_number)
#-----------------------------------------------------------------------------#
            # Caso "Avançado"
            elif str(self.ask_user) == "b": # Caso "Avançado"
                self.ask_user_number = input("Numero: ") # self.ask_number
                if self.ask_user_number.isalpha():
                    print(self.ask_user_number, "- Letras não são validas")
                else:
                    self.ask_user_type_1 = input("Opção: ") # self.ask_type1
                    self.ask_user_type_2 = input("Opção: ") # self.ask_type2
                    self.ask_user_type_3 = input("Opção: ") # self.ask_type3
                    self.ask_user_type_4 = input("Opção: ") # self.ask_type4
                    print(self.pass_custom(self.ask_user_number, 
                                           self.ask_user_type_1, 
                                           self.ask_user_type_2, 
                                           self.ask_user_type_3, 
                                           self.ask_user_type_4))
#-----------------------------------------------------------------------------#
    # Geração Fraca, Media, Forte, Insana
    def pass_all(self, ask_type, ask_number):
        self.ask_number = ask_number
        self.ask_type = ask_type
        if str(self.ask_type) == "fraca": # caso fraca
            if int(self.ask_number) > 26: 
                print(self.ask_number, 
"- É um numero muito grande, tente com numeros iguais ou menores que 26")
            else: 
                self.ask_type = self.s_lower
                print("".join(random.sample(self.ask_type, 
                              int(self.ask_number))))
        elif str(self.ask_type) == "media": # caso media
            if int(self.ask_number) > 52:
                print(self.ask_number, 
"- É um numero muito grande, tente com numeros iguais ou menores que 26")
            else:
                self.ask_type = self.s_letter
                print("".join(random.sample(self.ask_type, 
                              int(self.ask_number))))
        elif str(self.ask_type) == "forte": # caso forte
            if int(self.ask_number) > 62:
                print(self.ask_number, 
"- É um numero muito grande, tente com numeros iguais ou menores que 26")
            else:
                self.ask_type = self.s_letter + self.s_digits
                print("".join(random.sample(self.ask_type, 
                              int(self.ask_number))))
        elif str(self.ask_type) == "insana": # caso insana
            if int(self.ask_number) > 94:
                print(self.ask_number, 
"- É um numero muito grande, tente com numeros iguais ou menores que 26")
            else:
                self.ask_type = self.s_letter + self.s_digits + self.s_punctuation
                print("".join(random.sample(self.ask_type, 
                              int(self.ask_number))))
#-----------------------------------------------------------------------------#
    # Geração Avançada
    def pass_custom(self, ask_number, 
                          ask_type1="", 
                          ask_type2="", 
                          ask_type3="", 
                          ask_type4=""):

        self.ask_number = ask_number
        self.ask_type1 = self.ask_type_opt(ask_type1)
        self.ask_type2 = self.ask_type_opt(ask_type2)
        self.ask_type3 = self.ask_type_opt(ask_type3)
        self.ask_type4 = self.ask_type_opt(ask_type4)

        # Caso erro None, adicionar if self.ask_type1 == None:
        #                               pass
        # Ou também adicionar um try e except

        return "".join(random.sample(self.ask_type1 + 
                                     self.ask_type2 + 
                                     self.ask_type3 + 
                                     self.ask_type4, 
                                     int(self.ask_number)))
                             #-------#
    def ask_type_opt(self, x):
        self.x = x
        if str(self.x) == "lower":
            return self.s_lower
        if str(self.x) == "upper":
            return self.s_upper
        if str(self.x) == "digits":
            return self.s_digits
        if str(self.x) == "punctuation":
            return self.s_punctuation
        return self.x 
#-----------------------------------------------------------------------------#
















