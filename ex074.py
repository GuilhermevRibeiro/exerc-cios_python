"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla."""
import random
num = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))

print(f'Os números sorteados foram {num}')
print(f'O maior número é {max(num)} e o menor é {min(num)}')
