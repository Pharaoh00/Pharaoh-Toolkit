from modulos.passwordgeneretor import PasswordGenerator as Pass_Generetor 

ask_user = input("""
Opção MENU:
a. fraca
b. media
c. forte
d. insana
>> """)

Pass_Generetor = Pass_Generetor(ask_user, input("Numero: "))
print(Pass_Generetor.pass_all())








