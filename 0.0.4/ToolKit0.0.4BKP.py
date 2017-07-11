# ToolKit criado por Pharaoh
# Versão 0.0.5 (2017) [Ter, 11 Jul 19:12:03]
# Linguagem = PT-BR

# Novo na versão 0.0.4:
# Atualização para PEP8.
# Correção de bugs.
# Adicionado Fibonacci no mudulo Calculadora.
# Adicionado Numeros primos no modulo Calculadora.
# Adicionado nova opção no menu principal, python.
#
# -----------------------------------------------------------------------------------------------------------------------------------#
# Atualização PEP8:
# Adequando aos 4 espaços ao invez de tab.
# PasswordGenerator agora é Password_Generator.
# PassFraca agora é Pass_Fraca.
# PassMedia agora é Pass_Media.
# PassForte agora é Pass_Forte.
# PassInsana agora é Pass_Insana.
# PassCustom é Pass_Custom.
# askUser agora é ask_User
# letterStore agora é letter_Store
# finalPass agora é Final_Pass
# askOpt agora é ask_Opt
# askSqr agora é ask_Sqr
# -----------------------------------------------------------------------------------------------------------------------------------
# Correção de bugs:
# Gerador de senha - menu opções "Quantos caracteres você deseja ter?":
# Em todas as opções, fraca, media, forte, insana, custom apresentavam,
# erros com loop infinito.
# Caso o numero fosse maior que 72 ou 0 o programa entrava em loop.
# Opções de numero maximo das opções fraca, media, forte e insana fora
# adequadas ao numero maximo de possibilidades, para não ultrapassar o
# numero maximo da papulação random.sample().
#
# ---------------------------------------------------------------------------------------------------------------------------------
# Opção python MENU:
# Agora a opção utiliza sys.verion e sysconfig.get_platform() para obter informações sobre o python e o atual OS que está rodando.
#
import random
import sys
import string
import math
import time
import sysconfig

def main():
#-----------------------------------------------50---------------------------79---------------------------------------------------#
    # Modulo Gerador de Senha.
    def Password_Generator():
        # Titulo
        print("\nGerador de Senhas\n")
        # Titulo
        # INICIO FUNÇÕES DAS OPÇOES DO MENU
        #
        # Gerador para a senha "Fraca".
        def Pass_Fraca(x):
            letter_Store = string.ascii_lowercase # Letras de A a Z minusculas.
            print("") # Espaço.
            final_Pass = "".join(random.sample(letter_Store, int(x))) # Junção e Randomização.
            print("Essa senha está boa?: ", final_Pass,"\n")
        # Gerador para a senha "Media".
        def Pass_Media(x):
            letter_Store = string.ascii_letters # Letras de A a Z minusculas e Maiusculas.
            print("") # Espaço
            final_Pass = "".join(random.sample(letter_Store, int(x)))
            print("Essa senha está boa?: ", final_Pass,"\n")
        # Gerador para a senha "Forte".
        def Pass_Forte(x):
            letter_Store = string.ascii_letters + string.digits # Letrasde A a Z minusculas, Maiusculas e os numeros de 0 a 9.
            print("") # Espaço
            final_Pass = "".join(random.sample(letter_Store, int(x)))
            print("Essa senha está boa?: ", final_Pass,"\n")
        # Gerador para a senha "Insana".
        def Pass_Insana(x):
            letter_Store = string.ascii_letters + string.digits + string.punctuation # Letrasde A a Z minusculas, Maiusculas, os numeros de 0 a 9 e os caracteres especiais como "%" ou "$"
            print("") # Espaço
            final_Pass = "".join(random.sample(letter_Store, int(x)))
            print("Essa senha está boa?: ", final_Pass,"\n")
        # Gerador para "Custom".
        def Pass_Custom(a,b,c,d):
            try:
                enter = ""
                # Começo Bloco parametro A.
                if a != enter and b == enter and c == enter and d == enter: # Caso o slot 1 for diferente que "" Lettersore é igual "a", caso for numero, upper, lower ou espec "a" acaba se tornando umas das strings.
                    if a == "numero":
                        a = string.digits
                    if a == "upper":
                        a = string.ascii_uppercase
                    if a == "lower":
                        a = string.ascii_lowercase
                    if a == "espec":
                        a = string.punctuation
                    letter_Store = a # Somente se A for diferent.
                elif a != enter and b != enter and c == enter and d == enter:
                    if a == "numero":
                        a = string.digits
                    if a == "upper":
                        a = string.ascii_uppercase
                    if a == "lower":
                        a = string.ascii_lowercase
                    if a == "espec":
                        a = string.punctuation
                    #
                    if b == "numero":
                        b = string.digits
                    if b == "upper":
                        b = string.ascii_uppercase
                    if b == "lower":
                        b = string.ascii_lowercase
                    if b == "espec":
                        b = string.punctuation
                    letter_Store = a + b
                    #
                elif a != enter and b == enter and c != enter and d == enter:
                    if a == "numero":
                        a = string.digits
                    if a == "upper":
                        a = string.ascii_uppercase
                    if a == "lower":
                        a = string.ascii_lowercase
                    if a == "espec":
                        a = string.punctuation
                    #
                    if c == "numero":
                        c = string.digits
                    if c == "upper":
                        c = string.ascii_uppercase
                    if c == "lower":
                        c = string.ascii_lowercase
                    if c == "espec":
                        c = string.punctuation
                    letter_Store = a + c
                    #
                elif a != enter and b == enter and c == enter and d != enter:
                    if a == "numero":
                        a = string.digits
                    if a == "upper":
                        a = string.ascii_uppercase
                    if a == "lower":
                        a = string.ascii_lowercase
                    if a == "espec":
                        a = string.punctuation
                    #
                    if d == "numero":
                        d = string.digits
                    if d == "upper":
                        d = string.ascii_uppercase
                    if d == "lower":
                        d = string.ascii_lowercase
                    if d == "espec":
                        d = string.punctuation
                    letter_Store = a + d
                    #
                elif a != enter and b != enter and c != enter and d == enter:
                    if a == "numero":
                        a = string.digits
                    if a == "upper":
                        a = string.ascii_uppercase
                    if a == "lower":
                        a = string.ascii_lowercase
                    if a == "espec":
                        a = string.punctuation
                    #
                    if b == "numero":
                        b = string.digits
                    if b == "upper":
                        b = string.ascii_uppercase
                    if b == "lower":
                        b = string.ascii_lowercase
                    if b == "espec":
                        b = string.punctuation
                    #
                    if c == "numero":
                        c = string.digits
                    if c == "upper":
                        c = string.ascii_uppercase
                    if c == "lower":
                        c = string.ascii_lowercase
                    if c == "espec":
                        c = string.punctuation
                    letter_Store = a + b + c
                    #
                elif a != enter and b == enter and c != enter and d != enter:
                    if a == "numero":
                        a = string.digits
                    if a == "upper":
                        a = string.ascii_uppercase
                    if a == "lower":
                        a = string.ascii_lowercase
                    if a == "espec":
                        a = string.punctuation
                    #
                    if c == "numero":
                        c = string.digits
                    if c == "upper":
                        c = string.ascii_uppercase
                    if c == "lower":
                        c = string.ascii_lowercase
                    if c == "espec":
                        c = string.punctuation
                    #
                    if d == "numero":
                        d = string.digits
                    if d == "upper":
                        d = string.ascii_uppercase
                    if d == "lower":
                        d = string.ascii_lowercase
                    if d == "espec":
                        d = string.punctuation
                    letter_Store = a + c + d
                    #
                elif a != enter and b != enter and c != enter and d != enter:
                    if a == "numero":
                        a = string.digits
                    if a == "upper":
                        a = string.ascii_uppercase
                    if a == "lower":
                        a = string.ascii_lowercase
                    if a == "espec":
                        a = string.punctuation
                    #
                    if b == "numero":
                        b = string.digits
                    if b == "upper":
                        b = string.ascii_uppercase
                    if b == "lower":
                        b = string.ascii_lowercase
                    if b == "espec":
                        b = string.punctuation
                    #
                    if c == "numero":
                        c = string.digits
                    if c == "upper":
                        c = string.ascii_uppercase
                    if c == "lower":
                        c = string.ascii_lowercase
                    if c == "espec":
                        c = string.punctuation
                    #
                    if d == "numero":
                        d = string.digits
                    if d == "upper":
                        d = string.ascii_uppercase
                    if d == "lower":
                        d = string.ascii_lowercase
                    if d == "espec":
                        d = string.punctuation
                    letter_Store = a + b + c + d
                # Fim Bloco parametro A.
                # Começo Bloco parametro B.
                elif a == enter and b != enter and c == enter and d == enter:
                    if b == "numero":
                        b = string.digits
                    if b == "upper":
                        b = string.ascii_uppercase
                    if b == "lower":
                        b = string.ascii_lowercase
                    if b == "espec":
                        b = string.punctuation
                    letter_Store = b  # Somente se B for diferente.
                    #
                elif a == enter and b != enter and c != enter and d == enter:
                    if b == "numero":
                        b = string.digits
                    if b == "upper":
                        b = string.ascii_uppercase
                    if b == "lower":
                        b = string.ascii_lowercase
                    if b == "espec":
                        b = string.punctuation
                    #
                    if c == "numero":
                        c = string.digits
                    if c == "upper":
                        c = string.ascii_uppercase
                    if c == "lower":
                        c = string.ascii_lowercase
                    if c == "espec":
                        c = string.punctuation
                    letter_Store = b + c
                    #
                elif a == enter and b != enter and c == enter and d != enter:
                    if b == "numero":
                        b = string.digits
                    if b == "upper":
                        b = string.ascii_uppercase
                    if b == "lower":
                        b = string.ascii_lowercase
                    if b == "espec":
                        b = string.punctuation
                    #
                    if d == "numero":
                        d = string.digits
                    if d == "upper":
                        d = string.ascii_uppercase
                    if d == "lower":
                        d = string.ascii_lowercase
                    if d == "espec":
                        d = string.punctuation
                    letter_Store = b + d
                    #
                elif a == enter and b != enter and c != enter and d != enter:
                    if b == "numero":
                        b = string.digits
                    if b == "upper":
                        b = string.ascii_uppercase
                    if b == "lower":
                        b = string.ascii_lowercase
                    if b == "espec":
                        b = string.punctuation
                    #
                    if c == "numero":
                        c = string.digits
                    if c == "upper":
                        c = string.ascii_uppercase
                    if c == "lower":
                        c = string.ascii_lowercase
                    if c == "espec":
                        c = string.punctuation
                    #
                    if d == "numero":
                        d = string.digits
                    if d == "upper":
                        d = string.ascii_uppercase
                    if d == "lower":
                        d = string.ascii_lowercase
                    if d == "espec":
                        d = string.punctuation
                    letter_Store = b + c + d
                # Fim Bloco parametro B.
                # Começo Bloco parametro C.
                elif a == enter and b == enter and c != enter and d == enter:
                    if c == "numero":
                        c = string.digits
                    if c == "upper":
                        c = string.ascii_uppercase
                    if c == "lower":
                        c = string.ascii_lowercase
                    if c == "espec":
                        c = string.punctuation
                    letter_Store = c  # Somente se C for diferente.
                    #
                elif a == enter and b == enter and c != enter and d != enter:
                    if c == "numero":
                        c = string.digits
                    if c == "upper":
                        c = string.ascii_uppercase
                    if c == "lower":
                        c = string.ascii_lowercase
                    if c == "espec":
                        c = string.punctuation
                    #
                    if d == "numero":
                        d = string.digits
                    if d == "upper":
                        d = string.ascii_uppercase
                    if d == "lower":
                        d = string.ascii_lowercase
                    if d == "espec":
                        d = string.punctuation
                    letter_Store = c + d
                # Fim Bloco parametro C.
                # Começo Bloco parametro D.
                elif a == enter and b == enter and c == enter and d != enter:
                    if d == "numero":
                        d = string.digits
                    if d == "upper":
                        d = string.ascii_uppercase
                    if d == "lower":
                        d = string.ascii_lowercase
                    if d == "espec":
                        d = string.punctuation
                    letter_Store = d  # Somente se D for diferente.
                # Fim Bloco parametro D.
                print("") # Espaço
                final_Pass = "".join(random.sample(letter_Store, int(pass_Gen)))
                print("Essa sequencia está boa?: ", final_Pass,"\n")
            except ValueError:
                print("Provavelmente não tem tantos characteres quanto o tamanho final do valor.\nPor favor, adicione mais characteres ou tente um valor menor!")
            except TypeError:
                print("Você tem que passar algum argumento")
################################################################### FIM FUNÇÕES
        # Inicio comparações
        while(True):
            ask_Opt = str(input("Você quer uma senha fraca, media, forte, insana ou custom?: "))
            # Caso fraca
            if ask_Opt == "fraca":
                while(True):
                    pass_Gen = input("Quantos caracteres você deseja ter?(entre 1 a 26): ")
                    if str(pass_Gen) == "-v":
                        break
                    elif str(pass_Gen) == "exit":
                        sys.exit()
                    else:
                        try:
                            if int(pass_Gen) < 0:
                                print("Senhas com numeros negavitos não prestam!")
                            elif int(pass_Gen) == 0:
                                print("Não se pode ter uma senha com zero caracteres, não é mesmo?")
                            elif int(pass_Gen) > 26:
                                print("Não tente quebrar o programa!")
                            else:
                                Pass_Fraca(pass_Gen) # Chamando a funão Pass_Fraca(), que está la em cima.
                        except ValueError:
                            print("Somente numeros")
            # Caso media
            elif ask_Opt == "media":
                while(True):
                    pass_Gen = input("Quantos caracteres você deseja ter?(entre 1 a 52): ")
                    if str(pass_Gen) == "-v":
                        break
                    elif str(pass_Gen) == "exit":
                        sys.exit()
                    else:
                        try:
                            if int(pass_Gen) < 0:
                                print("Senhas com numeros negavitos não prestam!")
                            elif int(pass_Gen) == 0:
                                print("Não se pode ter uma senha com zero caracteres, não é mesmo?")
                            elif int(pass_Gen) > 52:
                                print("Não tente quebrar o programa!")
                            else:
                                Pass_Media(pass_Gen) # Chamando a funão Pass_Media(), que está la em cima.
                        except ValueError:
                            print("Somente numeros")
            # Caso forte
            elif ask_Opt == "forte":
                while(True):
                    pass_Gen = input("Quantos caracteres você deseja ter?(entre 1 a 62): ")
                    if str(pass_Gen) == "-v":
                        break
                    elif str(pass_Gen) == "exit":
                        sys.exit()
                    else:
                        try:
                            if int(pass_Gen) < 0:
                                print("Senhas com numeros negavitos não prestam!")
                            elif int(pass_Gen) == 0:
                                print("Não se pode ter uma senha com zero caracteres, não é mesmo?")
                            elif int(pass_Gen) > 62:
                                print("Não tente quebrar o programa!")
                            else:
                                Pass_Forte(pass_Gen) # Chamando a funão Pass_Forte(), que está la em cima.
                        except ValueError:
                            print("Somente numeros")
            # Caso insana
            elif ask_Opt == "insana":
                while(True):
                    pass_Gen = input("Quantos caracteres você deseja ter?(entre 1 a 94): ")
                    if str(pass_Gen) == "-v":
                        break
                    elif str(pass_Gen) == "exit":
                        sys.exit()
                    else:
                        try:
                            if int(pass_Gen) < 0:
                                print("Senhas com numeros negavitos não prestam!")
                            elif int(pass_Gen) == 0:
                                print("Não se pode ter uma senha com zero caracteres, não é mesmo?")
                            elif int(pass_Gen) > 94:
                                print("Não tente quebrar o programa!")
                            else:
                                Pass_Insana(pass_Gen) # Chamando a funão Pass_Insana(), que está la em cima.
                        except ValueError:
                            print("Somente numeros")
            # Caso custom
            elif ask_Opt == "custom":
                    while(True):
                        pass_Gen = input("Quantos caracteres você deseja ter?: ")
                        if str(pass_Gen) == "-v":
                            break
                        elif str(pass_Gen) == "exit":
                            sys.exit()
                        elif not pass_Gen.isdigit():
                            print("Somente numeros")
                        # Não esquecer de colocar maior q 72 menor e igual a 0.
                        else:
                            Pass_Custom(input("Slot 1: "),input("Slot 2: "),input("Slot 3: "),input("Slot 4: "))
            # Para sair do loop atual.
            elif ask_Opt == "-v":
                break
            # Para sair do programa.
            elif ask_Opt == "exit":
                print("\nSaindo do programa")
                sys.exit()
            else:
                print("Invalido")
            # Fim comparações
    # Fim modulo Geração de senha
# -----------------------------------------------------------------------------------------------------------------------------------#
# Inicio AJUDA
# -----------------------------------------------------------------------------------------------------------------------------------#
    def Ajuda():
        print("")
        print("")
        print("    ###          ## ##     ## ########     ###    ")
        time.sleep(0.1)
        print("   ## ##         ## ##     ## ##     ##   ## ##   ")
        time.sleep(0.1)
        print("  ##   ##        ## ##     ## ##     ##  ##   ##  ")
        time.sleep(0.1)
        print(" ##     ##       ## ##     ## ##     ## ##     ## ")
        time.sleep(0.1)
        print(" ######### ##    ## ##     ## ##     ## ######### ")
        time.sleep(0.1)
        print(" ##     ## ##    ## ##     ## ##     ## ##     ## ")
        time.sleep(0.1)
        print(" ##     ##  ######   #######  ########  ##     ## ")
        time.sleep(0.1)
        print("")
        print("")
        while(True):
            print("As opções disponiveis são:\n-help - Para obter mais informações.\npython Para obter informações sobre a versão do python instalada e em qual OS.\nexit - Para sair do programa.(Sai completamente do programa)\n-v - Para voltar as opções anteriores.")
            ask_User = input("O que desejar fazer?: ")
            if str(ask_User) == "-v":
                break
            elif str(ask_User) == "exit":
                sys.exit()
# -----------------------------------------------------------------------------------------------------------------------------------#
# Fim AJUDA
# -----------------------------------------------------------------------------------------------------------------------------------#
    # Modulo Calculadora
    def Calculadora():
        # Calculo numeros MDC e MMC
        def mmc(x,y):
            mdc = math.gcd(int(x),int(y))
            mmc = int(x) * int(y) // math.gcd(int(x),int(y))
            print("O MDC entre", str(x),"e",str(y),"é:", mdc)
            print("O MMC entre", str(x),"e",str(y),"é:", mmc)
        # Calculo numeros Fibonacci (Melhorar)
        def fib(x):
            a, b = 0, 1
            while a < int(x):
                print(a, end = ", ")
                a, b = b, a+b
            print("")
        # Calculo numero primo
        def prime(x):
            if x > 1:
                for i in range(2,x):
                    if x % i == 0:
                        print(x, "não é um primo") 
                        print("pois",x//i,"vezes",i,"é",x)
                        break
                else:
                    print(x, "é um numero primo")
            else:
                print(x, "não é um numero primo")
        # Sandbox
        def SandBox():
            print("O valor de PI é:", math.pi)
            while(True):
                try:
                    ask_User = input("Quanto é: ")
                    if str(ask_User) == "-v":
                        break
                    elif str(ask_User) == "exit":
                        sys.exit()
                    elif str(ask_User) == "-help":
                        print("\n-v para voltar.\nexit para sair.\nsqr para Raiz Quadrada.\nmdc ou mmc para Minimo Multiplo Comum ou Maximo Divisor Comum.\n(Qualquer uma das opções iram gerar tanto MMC quanto MDC)\nfib Para calcacular os numeros Fibonnaci\nprm Para checar se um numero é primo ou não\n")
                    # Raiz Quadrada
                    elif str(ask_User) == "sqr":
                        ask_Sqr = input("Raiz quadrada de: ")
                        ask_Sqr = math.sqrt(int(ask_Sqr))
                        print(ask_Sqr)
                    # MDC e MMC
                    elif str(ask_User) == "mdc" or str(ask_User) == "mmc":
                        mmc(input("Numero: "), input("Numero: "))
                    # Fibonacci
                    elif str(ask_User) == "fib":
                        fib(input("Fibonacci: "))
                    # Primos
                    elif str(ask_User) == "prm":
                        prime(input("Primo?: "))
                    else:
                        ask_User = eval(ask_User)
                        print(ask_User)
                except ZeroDivisionError:
                    print("Não se pode dividir por zero, lembra?")
                except SyntaxError:
                    print("Invalido - SyntaxError")
                except ValueError:
                    print("Invalido - ValueError")
                except NameError:
                    print("Invalido - NameError")
        SandBox()
# -----------------------------------------------------------------------------------------------------------------------------------#
# Fim modulo Calculadora
    # ANIMÇÃO DO INICIO DO PROGRAMA
    print("")
    print("")
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
    #
    # Para ajuda -help.
    print("\nPara mais informações -help")
    while(True):
        # MENU.
        print("___  ___ _____ _   _ _   _ ")
        print("|  \/  ||  ___| \ | | | | |")
        print("| .  . || |__ |  \| | | | |")
        print("| |\/| ||  __|| . ` | | | |")
        print("| |  | || |___| |\  | |_| |")
        print("\_|  |_/\____/\_| \_/\___/ ")
        print("")
        print("~~Ferramentas~~\n\n1. ~~Gerador de senha~\n2. ~~Calculadora~~\n")
        ask_User = input("O que deseja fazer? ")
        # -help.
        if str(ask_User) == "-help":
            Ajuda()
        # Para sair do programa.
        elif str(ask_User) == "exit":
            print("\nSaindo do programa!")
            time.sleep(0.2)
            sys.exit()
        elif str(ask_User) == "python":
            print("")
            print("Você está rodando python na versão:", sys.version)
            print("Você está rodando:",sysconfig.get_platform())
            print("")
        try:
            # Modulo Gerador de Senha.
            if int(ask_User) == 1:
                Password_Generator()
            # Modulo Calculadora.
            elif int(ask_User) == 2:
                Calculadora()
        except ValueError:
            print("Somente as opções a cima, para mais informações -help")

#                        #
# Chamando todo o programa.
main() #################
####
##
#
