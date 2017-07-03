import sys, time

def main():
	print("Isso é um teste, param mais informações -help","\nPara sair ctrl+c ou exit")
	while(True):
		print("\nFerramentas:\n","1.Password Generator\n","2.Calculator\n","3.Fiboccini\n")
		x = input("O que você desejar fazer? ")
		if x != "1" and x != "2" and x != "3" and x != "exit":
			print("Please use one of the numbers on menu")
		elif x == "exit":
			sys.exit()
		elif x == "1":
			while(True):
				y = input("Do you want it to be a weak, medium or insane password? ")

				if y != "weak" and y !=  "medium" and y != "strong" and y != "insane" and y != "-help" and y != "exit":
					print("please use wak/medium/strong/insane\n")
				elif y == "weak":
					print("weak\n")
				elif y == "medium":
					print("medium\n")
				elif y == "strong":
					print("strong\n")
				elif y == "insane":
					print("insane\n")
				elif y == "-help":
					print("Obrigado por usar esse programa")
					break
				elif y == "exit":
					print("Você está saindo do programa")
					time.sleep(1)
					sys.exit()
		elif x == "No":
			print("Ok, obrigado")
			sys.exit()

main()
