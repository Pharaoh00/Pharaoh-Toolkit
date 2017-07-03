import random, string
import sys

print("Password Generator\n")
userInput = input("Qual o tamanho da sua senha? ")

def passGen(x):
	if userInput.isdigit():
		specialsChar =".-_+*&#$@!%"
		letterStore = string.ascii_letters + string.digits + specialsChar
		print("".join(random.sample(letterStore, int(x) )))
	else:
		print("Somente numeros")

passGen(userInput)
