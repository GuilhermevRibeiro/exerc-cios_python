"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""



while True:
    n = int(input('Digite um número que deseja saber a tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} * {c} = {n*c}')
print('fim')


