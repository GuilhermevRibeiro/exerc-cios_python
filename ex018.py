"""Faça um programa que leia um ângulo qwualquer e mostre na tela o valor do seno, cosseno e da tangente desse ângulo"""

from math import radians, cos, sin, tan

angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o seno de {seno}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o cosseno de {cosseno}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a tangente de {tangente}')