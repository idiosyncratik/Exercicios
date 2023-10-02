# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00
# se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
# compradas, calcule e escreva o custo total da compra.
qtd_macas = int(input("Digite o número de maçãs compradas: "))
if qtd_macas < 12:
    custo = qtd_macas * 1.30
else:
    custo = qtd_macas * 1.00
print(f'O custo total da compra é {custo}R$')