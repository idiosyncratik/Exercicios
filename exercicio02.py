#Crie um código que leia um número diferente de zero e diga se este número é positivo ou negativo
num = int(input("Digite um número diferente de 0: "))
if num > 0:
    print(f'O número {num} é positivo.')
elif num < 0:
    print(f'O número {num} é negativo.')
else:
    print("Número inválido.")