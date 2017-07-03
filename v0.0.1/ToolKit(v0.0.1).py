import random, time
import string, sys

def main():
	# Modulo Gerador de Senha.
	def PasswordGenerator():
		# Gerador para a senha "Fraca".
		def PassFraca():
			letterStore = string.ascii_lowercase # Letras de A a Z minusculas.
			print("") # Espaço.
			print("".join(random.sample(letterStore, int(passGen)))) # Junção e Randomização.
			return True # Failsafe?.
		# Gerador para a senha "Media".
		def PassMedia():
			letterStore = string.ascii_letters # Letras de A a Z minusculas e Maiusculas.
			print("")
			print("".join(random.sample(letterStore, int(passGen))))
			return True
		# Gerador para a senha "Forte".
		def PassForte():
			letterStore = string.ascii_letters + string.digits # Letrasde A a Z minusculas, Maiusculas e os numeros de 0 a 9.
			print("")
			print("".join(random.sample(letterStore, int(passGen))))
			return True
		# Gerador para a senha "Insana".
		def PassInsana():
			letterStore = string.ascii_letters + string.digits + string.punctuation # Letrasde A a Z minusculas, Maiusculas, os numeros de 0 a 9 e os caracteres especiais como "%" ou "$"
			print("")
			print("".join(random.sample(letterStore, int(passGen))))
			return True

		print("\nGerador de Senhas\n")
		while(True):
			#FailSafe?
			try:
				passGen = input("Qual o tamanho da sua senha? (Entre 1 a 72): ")
				if str(passGen) == "exit":
					print("\nSaindo do programa!")
					sys.exit() # sys.exit() = Sair de tudo.
				elif str(passGen) == "-v":
					break # break = Sair somente do loop atual.
				elif int(passGen) == 0:
					print("\nNão se pode ter uma senha com zero numeros, não é mesmo?\n") # Uma brincadeirinha.
				elif int(passGen) > 72:
					print("\nNão tente quebrar o meu programa!\n") # Outra brincadeirinha.
				else:
					while(True):
						askOpt = str(input("-v ~~Para voltar a escolher o tamanho da senha\nVocê quer uma senha fraca, media, forte ou insana?: "))
						# Caso fraca.
						if askOpt == "fraca":
							while(True):
								PassFraca() # Chamando a funão PassFraca(), que está la em cima.
								askUser = str(input("\nEssa senha está boa?\nCaso SIM, s para sair!\nCaso NAO, aperte qualquer tecla!: "))
								if askUser == "s":
									break # Para sair do loop atual.
								elif askUser == "exit":
									sys.exit() # Para sair de todo o programa.
						# Caso media.
						elif askOpt == "media":
							while(True):
								PassMedia()
								askUser = str(input("\nEssa senha está boa?\nCaso SIM, s para sair!\nCaso NAO, aperte qualquer tecla!: "))
								if askUser == "s":
									break
								elif askUser == "exit":
									sys.exit()
						# Caso forte.
						elif askOpt == "forte":
							while(True):
								PassForte()
								askUser = str(input("\nEssa senha está boa?\nCaso SIM, s para sair!\nCaso NAO, aperte qualquer tecla!: "))
								if askUser == "s":
									break
								elif askUser == "exit":
									sys.exit()
						# Caso insana.
						elif askOpt == "insana":
							while(True):
								PassInsana()
								askUser = str(input("\nEssa senha está boa?\nCaso SIM, s para sair!\nCaso NAO, aperte qualquer tecla!: "))
								if askUser == "s":
									break
								elif askUser == "exit":
									sys.exit()
						# Para sair do loop atual.
						elif askOpt == "-v":
							break
						# Para sair do programa.
						elif askOpt == "exit":
							print("\nSaindo do programa")
							sys.exit()
						else:
							print("\n~~Somente as opções a cima, fraca, media, forte, insana~~\n")	
			# Caso der algum erro.
			except ValueError:
				print("\n~~Somente numeros!!~~\n")
			# Caso der algum erro.
			except NameError:
				print("\n~~Somente numeros!~~\n")

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

	# Para ajuda -help.
	print("\nPara mais informações -help")
	while(True):
		#FailSafe?.
		try:
			# MENU.
			print("~~Ferramentas~~\n\n1. ~~Gerador de senha~\n2. ~~Calculadora~~\n")
			askUser = input("O que deseja fazer? ")
			# -help.
			if str(askUser) == "-help":
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
			# Para sair do programa.
			elif str(askUser) == "exit":
				print("\nSaindo do programa!")
				time.sleep(0.2)
				sys.exit()
			# Modulo Gerador de Senha.
			elif int(askUser) == 1:
				PasswordGenerator()
			# Modulo Calculadora.
			elif int(askUser) == 2:
				return True
		# Caso der algum erro.
		except ValueError:
			print("\n~~Somente as opções a cima.\nPara mais informações -help~~\n")

# Chamando todo o programa.
main()
