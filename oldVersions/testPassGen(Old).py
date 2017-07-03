import random, string


def PassCustom():
	try:
		passGen = input("Quantos caracteres você deseja ter?: ")
		
		if a == "numeros" or b == "numeros" or c == "numeros" or d == "numeros" or e == "numeros":
			a = string.digits
			b = string.digits
			c = string.digits
			d = string.digits
			e = string.digits
		if a == "upper" or b == "upper" or c == "upper" or d == "upper" or e == "upper":
			a = string.ascii_uppercase
			b = string.ascii_uppercase
			c = string.ascii_uppercase
			d = string.ascii_uppercase
			e = string.ascii_uppercase

		a = input("Slot 1: ")
		b = input("Slot 2: ")
		c = input("Slot 3: ")
		d = input("Slot 4: ")
		e = input("Slot 5: ")

		letterStore = a + b + c + d + e

		print("".join(random.sample(letterStore, int(passGen))))
		return True
	except ValueError:
		print("Provavelmente não tem tantos characteres quanto o tamanho final do valor.\nPor favor, adicione mais characteres ou tente um valor menor!")
	except TypeError:
		print("Você tem que passar algum argumento")
	except UnboundLocalError:
		print("Precisa de algum parametro")

PassCustom()
