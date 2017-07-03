import random, string
import sys


def PassCustom(a,b,c,d):
	try:
		enter = ""
		# Começo Bloco parametro A.
		if a != enter and b == enter and c == enter and d == enter:
			if a == "numero":
				a = string.digits
			if a == "upper":
				a = string.ascii_uppercase
			if a == "lower":
				a = string.ascii_lowercase
			if a == "espec":
				a = string.punctuation
			letterStore = a # Somente se A for diferent.

		elif a != enter and b != enter and c == enter and d == enter:
			if a == "numero":
				a = string.digits
			if a == "upper":
				a = string.ascii_uppercase
			if a == "lower":
				a = string.ascii_lowercase
			if a == "espec":
				a = string.punctuation

			if b == "numero":
				b = string.digits
			if b == "upper":
				b = string.ascii_uppercase
			if b == "lower":
				b = string.ascii_lowercase
			if b == "espec":
				b = string.punctuation
			letterStore = a + b

		elif a != enter and b == enter and c != enter and d == enter:
			if a == "numero":
				a = string.digits
			if a == "upper":
				a = string.ascii_uppercase
			if a == "lower":
				a = string.ascii_lowercase
			if a == "espec":
				a = string.punctuation

			if c == "numero":
				c = string.digits
			if c == "upper":
				c = string.ascii_uppercase
			if c == "lower":
				c = string.ascii_lowercase
			if c == "espec":
				c = string.punctuation
			letterStore = a + c

		elif a != enter and b == enter and c == enter and d != enter:
			if a == "numero":
				a = string.digits
			if a == "upper":
				a = string.ascii_uppercase
			if a == "lower":
				a = string.ascii_lowercase
			if a == "espec":
				a = string.punctuation

			if d == "numeros":
				d = string.digits
			if d == "upper":
				d = string.ascii_uppercase
			if d == "lower":
				d = string.ascii_lowercase
			if d == "espec":
				d = string.punctuation
			letterStore = a + d
		elif a != enter and b != enter and c != enter and d == enter:
			if a == "numero":
				a = string.digits
			if a == "upper":
				a = string.ascii_uppercase
			if a == "lower":
				a = string.ascii_lowercase
			if a == "espec":
				a = string.punctuation

			if b == "numeros":
				b = string.digits
			if b == "upper":
				b = string.ascii_uppercase
			if b == "lower":
				b = string.ascii_lowercase
			if b == "espec":
				b = string.punctuation

			if c == "numero":
				c = string.digits
			if c == "upper":
				c = string.ascii_uppercase
			if c == "lower":
				c = string.ascii_lowercase
			if c == "espec":
				c = string.punctuation
			letterStore = a + b + c

		elif a != enter and b == enter and c != enter and d != enter:
			if a == "numero":
				a = string.digits
			if a == "upper":
				a = string.ascii_uppercase
			if a == "lower":
				a = string.ascii_lowercase
			if a == "espec":
				a = string.punctuation

			if c == "numero":
				c = string.digits
			if c == "upper":
				c = string.ascii_uppercase
			if c == "lower":
				c = string.ascii_lowercase
			if c == "espec":
				c = string.punctuation

			if d == "numero":
				d = string.digits
			if d == "upper":
				d = string.ascii_uppercase
			if d == "lower":
				d = string.ascii_lowercase
			if d == "espec":
				d = string.punctuation
			letterStore = a + c + d

		elif a != enter and b != enter and c != enter and d != enter:
			if a == "numero":
				a = string.digits
			if a == "upper":
				a = string.ascii_uppercase
			if a == "lower":
				a = string.ascii_lowercase
			if a == "espec":
				a = string.punctuation

			if b == "numero":
				b = string.digits
			if b == "upper":
				b = string.ascii_uppercase
			if b == "lower":
				b = string.ascii_lowercase
			if b == "espec":
				b = string.punctuation

			if c == "numero":
				c = string.digits
			if c == "upper":
				c = string.ascii_uppercase
			if c == "lower":
				c = string.ascii_lowercase
			if c == "espec":
				c = string.punctuation

			if d == "numero":
				d = string.digits
			if d == "upper":
				d = string.ascii_uppercase
			if d == "lower":
				d = string.ascii_lowercase
			if d == "espec":
				d = string.punctuation
			letterStore = a + b + c + d
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
			letterStore = b  # Somente se B for diferente.

		elif a == enter and b != enter and c != enter and d == enter:
			if b == "numero":
				b = string.digits
			if b == "upper":
				b = string.ascii_uppercase
			if b == "lower":
				b = string.ascii_lowercase
			if b == "espec":
				b = string.punctuation

			if c == "numero":
				c = string.digits
			if c == "upper":
				c = string.ascii_uppercase
			if c == "lower":
				c = string.ascii_lowercase
			if c == "espec":
				c = string.punctuation
			letterStore = b + c

		elif a == enter and b != enter and c == enter and d != enter:
			if b == "numero":
				b = string.digits
			if b == "upper":
				b = string.ascii_uppercase
			if b == "lower":
				b = string.ascii_lowercase
			if b == "espec":
				b = string.punctuation

			if d == "numero":
				d = string.digits
			if d == "upper":
				d = string.ascii_uppercase
			if d == "lower":
				d = string.ascii_lowercase
			if d == "espec":
				d = string.punctuation
			letterStore = b + d

		elif a == enter and b != enter and c != enter and d != enter:
			if b == "numero":
				b = string.digits
			if b == "upper":
				b = string.ascii_uppercase
			if b == "lower":
				b = string.ascii_lowercase
			if b == "espec":
				b = string.punctuation

			if c == "numero":
				c = string.digits
			if c == "upper":
				c = string.ascii_uppercase
			if c == "lower":
				c = string.ascii_lowercase
			if c == "espec":
				c = string.punctuation

			if d == "numero":
				d = string.digits
			if d == "upper":
				d = string.ascii_uppercase
			if d == "lower":
				d = string.ascii_lowercase
			if d == "espec":
				d = string.punctuation
			letterStore = b + c + d
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
			letterStore = c  # Somente se C for diferente.

		elif a == enter and b == enter and c != enter and d != enter:
			if c == "numero":
				c = string.digits
			if c == "upper":
				c = string.ascii_uppercase
			if c == "lower":
				c = string.ascii_lowercase
			if c == "espec":
				c = string.punctuation

			if d == "numero":
				d = string.digits
			if d == "upper":
				d = string.ascii_uppercase
			if d == "lower":
				d = string.ascii_lowercase
			if d == "espec":
				d = string.punctuation
			letterStore = c + d
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
			letterStore = d  # Somente se D for diferente.
		# Fim Bloco parametro D.

		print("".join(random.sample(letterStore, int(passGen))))
		return True
	except ValueError:
		print("Provavelmente não tem tantos characteres quanto o tamanho final do valor.\nPor favor, adicione mais characteres ou tente um valor menor!")
	except TypeError:
		print("Você tem que passar algum argumento")


passGen = input("Quantos caracteres você deseja ter?: ")
if not passGen.isdigit():
	print("Somente numeros")
else:
	PassCustom(input("Slot 1: "),input("Slot 2: "),input("Slot 3: "),input("Slot 4: "))
