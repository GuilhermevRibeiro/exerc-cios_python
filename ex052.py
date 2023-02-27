#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
cont = 0
n = int(input('Digite um número inteiro:'))
for c in range(1, n+1):
    if n % c==0:
        cont = cont + 1
if cont == 2:
    print(f'O número {n} foi dividido {cont} vezes, portanto é primo')
else:
    print('O número não é primo')