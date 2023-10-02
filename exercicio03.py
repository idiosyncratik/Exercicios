#Crie um código que leia a idade de uma pessoa e diga em qual ano ela nasceu
mesatual = int(input("Digite o mês atual: "))
idade = int(input("Digite a sua idade: "))
mesnasc = int(input("Digite o mês em que você faz aniversário: "))
ano = 2023-idade
if mesnasc >= mesatual:
    print(f'Você nasceu em: {ano-1}')
else:
    print(f'Você nasceu em: {ano}')