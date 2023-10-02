#Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10,
# caso contrário escrever NÃO É MAIOR QUE 10!
valor = int(input("Digite um valor: "))

if valor >= 10:
    print(f'{valor} é maior que 10!')
else:
    print(f'{valor} não é maior que 10!')