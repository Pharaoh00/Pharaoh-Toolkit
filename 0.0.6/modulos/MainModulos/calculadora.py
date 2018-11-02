#!-*- coding:utf-8 -*-
import math
import sys
from .prototypeformat import *
formating = FormatString()
#-----------------------------------------------------------------------------#
# OOP Calculadora
class Calculadora:
    is_done = False
    menu = ["",
            "Opções:",
            "exit",
            "-v",
            "mmc/mdc",
            "fib",
            "prm",
            ""]

    def __init__(self):
        self.calculadora_menu()
    
    def calculadora_menu(self):
        print("")
        print(formating.formatCenter("Modulo Calculadora", "CENTER"))
        print("O valor de PI é:", math.pi)
        while not self.is_done:
            print("Para ajuda -help")
            self.ask_user = input(formating.formatDate("O que deseja fazer?: "))
            if str(self.ask_user) == "exit":
                print("Saindo...")
                sys.exit()
            elif str(self.ask_user) == "-v":
                print("Voltando...")
                self.is_done = True
            elif str(self.ask_user) == "-help":
                print(formating.formatMenu(self.menu))
            elif str(self.ask_user) == "mmc" or str(self.ask_user) == "mdc":
                self.ask_opt_1 = input("Numero: ")
                self.ask_opt_2 = input("Numero: ")
                self.calc_mmc(self.ask_opt_1, self.ask_opt_2)
            elif str(self.ask_user) == "fib":
                self.ask_fib = input("Fibonacci: ")
                self.calc_fib(self.ask_fib)
            elif str(self.ask_user) == "prm":
                self.ask_prm = int(input("Primo?: "))
                self.calc_prime(self.ask_prm)
            elif str(self.ask_user) == "sqr":
                self.ask_sqr = input("A raiz quadrada de: ")
                self.ask_sqr = math.sqrt(int(self.ask_sqr))
                print(self.ask_sqr)
            else:
                self.ask_user = eval(self.ask_user)
                print(self.ask_user)

#-----------------------------------------------------------------------------#
    def calc_mmc(self, calc_x, calc_y):
        self.calc_x = calc_x
        self.calc_y = calc_y
        mdc = math.gcd(int(self.calc_x),int(self.calc_y))
        mmc = int(self.calc_x) * int(self.calc_y) // math.gcd(int(self.calc_x),
                                                              int(self.calc_y))
        print("O MDC entre", str(self.calc_x),"e",str(self.calc_y),"Ã©:", mdc)
        print("O MMC entre", str(self.calc_x),"e",str(self.calc_y),"Ã©:", mmc)
#-----------------------------------------------------------------------------#
    def calc_fib(self, calc_x):
        self.calc_x = calc_x
        self.a, self.b = 0, 1
        while self.a < int(self.calc_x):
            print(self.a, end = ", ")
            self.a, self.b = self.b, self.a + self.b
        print("")
#-----------------------------------------------------------------------------#
    # --> BUG <--
    # ApÃ³s fazer o primeiro calculo, o programa quebra.
    # "prm" is note definied
    def calc_prime(self, calc_x):
        self.calc_x = calc_x
        if self.calc_x > 1:
            for self.i in range(2,self.calc_x):
                if self.calc_x % self.i == 0:
                   print(self.calc_x, "nÃ£o Ã© um primo") 
                   print("pois",self.calc_x//self.i,"vezes",self.i,"Ã©",self.calc_x)
                   break
            else:
                print(self.calc_x, "Ã© um numero primo")
        else:
            print(self.calc_x, "nÃ£o Ã© um numero primo")
