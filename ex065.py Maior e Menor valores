"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar."""

resposta = 'S'
media = cont = soma = maior = menor = 0

while resposta == 'S':
    num = int(input('Digite um número qualquer: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
print('fim')
media = soma/cont
print(f'A média dos {cont} números digitados é {media}')
print(f'O maior número é {maior} e o menor é {menor}')
