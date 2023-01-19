"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
0,50 por Km para viagens de até 200km e 0,45 para viagens mais longas."""

distancia = float(input('Qual a distância da sua viagem: '))

if distancia <= 200:
    print(f'A sua viagem é de {distancia} Kms, o preço será de R${distancia*0.50}')
else:
    print(f"A sua viagem é de {distancia} Kms, o preço será de R${distancia*0.45}")
