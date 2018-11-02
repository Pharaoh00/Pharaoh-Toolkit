#!-*- coding:utf-8 -*-
#implementation.py

from MainModulos import prototypeformat
formating = prototypeformat.FormatString()

def calc_menu():
    menu = ["exit - (Para sair)",
            "-v - (Para voltar)",
            "mmc/mdc - (Para calcular mmc/mdc)",
            "fib - (Para calcular fibonnaci)",
            "prm - (Para calculador nº primos"]
    running = True

    #print("\n".join(map(str, menu)))
    print("Para ajuda -help")
    while running:
        user = input(formating.formatDate(""))
    print(formating.formatMenu(menu), end="")

calc_menu()
