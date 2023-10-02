#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias
#e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e
# mês com 30 dias
anos = int(input("Digite a sua idade: "))
mes = int(input("Digite o mês do seu aniversário: "))
dia = int(input("Digite o dia do seu aniversário: "))
idade_em_dias = anos * 365 + mes * 30 + dia
print(f'Você tem {idade_em_dias} dias de vida.')