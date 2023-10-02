#Crie um algoritmo que leia um número e diga se ele é par ou ímpar
num = int(input("Digite um número: "))
resto_da_divisao = num%2
if resto_da_divisao==0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é impar.')