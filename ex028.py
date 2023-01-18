"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
perdeu."""
import random
numero = random.randint(0, 5)

print('Vou pensar num número entre 0 e 5, tente adivinhar!')

usuario = int(input("Em qual número você acha que eu pensei: "))

if usuario == numero:
    print('Parabéns, você acertou!')
else:
    print(f'Hmmm, não foi dessa vez, na verdade o número que eu pensei foi {numero}')