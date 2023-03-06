#Faça um programa que leia um número qualquer e mostre o seu fatorial
import math
num = int(input('Digite o número para calcular seu fatorial: '))
fac = math.factorial(num)
print(f'O fatorial de {num} é {fac}')