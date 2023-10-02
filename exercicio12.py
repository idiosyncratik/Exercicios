# Escreva um algoritmo para ler o número total de eleitores de um município, o
# número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada
# um representa em relação ao total de eleitores.
eleitores = int(input("Digite o número de eleitores do município: "))
brancos = int(input("Digite o número de votos brancos: "))
nulos = int(input("Digite o número de votos nulos: "))
validos = int(input("Digite o número de votos válidos: "))

percentual_brancos = (brancos / eleitores) * 100
percentual_nulos = (nulos / eleitores) * 100
percentual_validos = (validos / eleitores) * 100

print(f'O percentual de votos em branco é de {percentual_brancos}%')
print(f'O percentual de votos nulos é de {percentual_nulos}%')
print(f'O percentual de votos válidos é de {percentual_validos}%')