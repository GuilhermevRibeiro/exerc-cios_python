#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

num = int(input('Digite um número: '))
calc = num % 2

if calc == 1:
    print('O número é ímpar')
else:
    print('O número é par')