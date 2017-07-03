import sys

def main():
	def Calculator():
		def Adicao(x,y):
			if x == "" or y == "":
				print("Tem que passar algum numero")
			print(float(x)+float(y))
		def Subitracao(x,y):
			if x == "" or y == "":
				print("Tem que passar algum numero")
			print(float(x)-float(y))
		def Multiplicacao(x,y):
			if x == "" or y == "":
				print("Tem que passar algum numero")
			print(float(x)*float(y))
		def Divicao(x,y):
			if x == "" or y == "":
				print("Tem que passar algum numero")
			print(float(x)/float(y))

		print("Calculadora")
		while(True):
			askUser = input("a. Adicão\nb. Subitração\nc. Multiplicação\nd. Divisão\nO que desejar fazer?: ")
			if str(askUser) == "a":
				Adicao(input("Numero: "),input("Numero: "))
			elif str(askUser) == "b":
				Subitracao(input("Numero: "), input("Numero: "))
			elif str(askUser) == "c":
				Multiplicacao(input("Numero: "), input("Numero: "))
			elif str(askUser) == "d":
				Divicao(input("Numero: "), input("Numero: "))
			elif str(askUser) == "exit":
				sys.exit()
			elif askUser.isdigit():
				print("\nSomente as opções a cima\n")

	Calculator()
main()
