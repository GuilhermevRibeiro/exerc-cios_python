"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa. """
import math

cateto_opo = float(input('Comprimento oposto: '))
cateto_adj = float(input('Comprimento adjacente: '))
h1 = math.hypot(cateto_opo, cateto_adj)
print(f'A hipotenusa mede: {h1}')
