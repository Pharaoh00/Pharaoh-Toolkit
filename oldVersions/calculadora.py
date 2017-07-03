
import math
import sys, string

def Calculadora():
	def SandBox():
		print("O valor de PI é:", math.pi)
		while(True):
			try:
				askUser = input("Quanto é: ")
				if str(askUser) == "-v":
					break
				elif str(askUser) == "exit":
					sys.exit()
				elif str(askUser) == "-help":
					print("\n-v para voltar.\nexit para sair.\nsqr para Raiz Quadrada.\nmdc ou mmc para Minimo Multiplo Comum ou Maximo Divisor Comum.\n(Qualquer uma das opções iram gerar tanto MMC quanto MDC)\n")
				elif str(askUser) == "sqr":
					askSqr = input("Raiz quadrada de: ")
					askSqr = math.sqrt(int(askSqr))
					print(askSqr)
				elif str(askUser) == "mdc" or str(askUser) == "mmc":
					slot1 = input("Numero: ")
					slot2 = input("Numero: ")
					mdc = math.gcd(int(slot1),int(slot2))
					mmc = int(slot1) * int(slot2) // math.gcd(int(slot1),int(slot2))
					print("O MDC entre", str(slot1),"e",str(slot2),"é:", mdc)
					print("O MMC entre", str(slot1),"e",str(slot2),"é:", mmc)
				else:
					askUser = eval(askUser)
					print(askUser)
			except ZeroDivisionError:
				print("Não se pode dividir por zero, lembra?")
			except SyntaxError:
				print("Invalido - SyntaxError")
			except ValueError:
				print("Invalido - ValueError")
			except NameError:
				print("Invalido - NameError")

	SandBox()
Calculadora()
