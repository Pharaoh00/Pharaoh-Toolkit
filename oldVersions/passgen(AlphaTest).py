import random, string, sys, time


def PasswordGenerator():
	def PassFraca():
		letterStore = string.ascii_lowercase
		print("\n")
		print("".join(random.sample(letterStore, int(passGen))))
		return True
	def PassMedia():
		letterStore = string.ascii_letters
		print("\n")
		print("".join(random.sample(letterStore, int(passGen))))
		return True
	def PassForte():
		letterStore = string.ascii_letters + string.digits
		print("\n")
		print("".join(random.sample(letterStore, int(passGen))))
		return True
	def PassInsana():
		letterStore = string.ascii_letters + string.digits + string.punctuation
		print("\n")
		print("".join(random.sample(letterStore, int(passGen))))
		return True

	print("\nGerador de Senhas\n")
	while(True):
		passGen = input("Qual o tamanho da sua senha? (Entre 1 a 72): ")
		if not passGen.isdigit() and str(passGen) != "-v" and str(passGen) != "exit":
			print("\nSomente numeros\n")
		elif str(passGen) == "exit":
			print("\nSaindo do programa!")
			sys.exit()
		elif str(passGen) == "-v":
			break
		elif int(passGen) == 0:
			print("\nNão se pode ter uma senha com zero numeros, não é mesmo?\n")
		elif int(passGen) > 72:
			print("\nNão tente quebrar o meu programa!\n")
		else:
			while(True):
				askOpt = str(input("\n-v ~~ Para voltar a escolher o tamanho da senha\nVocê quer uma senha fraca, media, forte ou insana?: "))
				if askOpt != "fraca" and askOpt != "media" and askOpt != "forte" and askOpt != "insana" and askOpt != "exit" and askOpt != "-v" and askOpt != "exit":
					print("Somente as opções a cima, fraca, media, forte, insana")
				elif askOpt == "fraca":
					while(True):
						PassFraca()
						askUser = str(input("\nEssa senha está boa?\nCaso SIM, s para sair!\nCaso NAO, aperte qualquer tecla!: "))
						if askUser == "s":
							break
						elif askUser == "exit":
							sys.exit()
				elif askOpt == "media":
					while(True):
						PassMedia()
						askUser = str(input("\nEssa senha está boa?\nCaso SIM, s para sair!\nCaso NAO, aperte qualquer tecla!: "))
						if askUser == "s":
							break
						elif askUser == "exit":
							sys.exit()
				elif askOpt == "forte":
					while(True):
						PassForte()
						askUser = str(input("\nEssa senha está boa?\nCaso SIM, s para sair!\nCaso NAO, aperte qualquer tecla!: "))
						if askUser == "s":
							break
						elif askUser == "exit":
							sys.exit()
				elif askOpt == "insana":
					while(True):
						PassInsana()
						askUser = str(input("\nEssa senha está boa?\nCaso SIM, s para sair!\nCaso NAO, aperte qualquer tecla!: "))
						if askUser == "s":
							break
						elif askUser == "exit":
							sys.exit()
				elif askOpt == "-v":
					break
				elif askOpt == "exit":
					print("\nSaindo do programa")
					sys.exit()


PasswordGenerator()
