import random

names_list = ['Abdul', 'Alia', 'Alla', 'Andree', 'Armando', 'Ashley', 'August', 'Bebe', 'Candi', 'Candie', 'Clarine', 'Daria', 'Dorie', 'Dusti', 'Eun', 'Gertha', 'Gilbert', 'Grant', 'Gwyneth', 'Ha', 'Hyun', 'Isadora', 'Jacklyn', 'Jenell', 'Jerrell', 'Jesse', 'Judson', 'Jutta', 'Karie', 'Kristi', 'Laine', 'Loni', 'Lula', 'Lura', 'Malena', 'Marcelle', 'Ofelia', 'Omega', 'Reed', 'Ronda', 'Sarina', 'Shelly', 'Shenita', 'Sherise', 'Stacey', 'Tama', 'Tia', 'Velvet', 'Verlene', 'Walton']

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]

name, sheres, price, date = data

new_list = []

list_input = str(input("Letra: "))
# Sem lista
for i in range(len(names_list)):
    check = names_list[i].startswith(list_input)
    if check == True:
        print(names_list[i])
# Com lista
for i in range(len(names_list)):
    check = names_list[i].startswith(list_input)
    if check == True:
        new_list.append(names_list[i])
print(random.choice(new_list))
# Com random
#for i in range(len(names_list)):
#    check = names_list[i].startswith("A")
#    if check == True:
#        new_list.append(names_list[i])
#print(random.choice(new_list))

# Colocando a lista em ordem alphabetica ou numerica
#print(sorted(names_list))

# Checando se a primeira letra do index [0] começa com a letra C
#if names_list[0].startswith("C") == True: 
#    print(names_list[0])   



# Contando quantas letras a em uma palavra
#def count_letters(word):
#    return len(word)
#
#print(count_letters(names_list[0]))

