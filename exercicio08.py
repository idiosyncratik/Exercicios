# Faça um código que receba 4 números e realize a soma deles e a média entre eles.
# e mostre os resultados.
soma = 0
for x in range(4):
    num = float(input("Digite o número: "))
    soma = soma+num
media = soma/4
print(soma)
print(media)