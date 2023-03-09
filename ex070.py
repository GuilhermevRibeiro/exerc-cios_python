"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar. No final, mostre:
a) total gasto na compra
b) quantos produtos custam mais de R$1000.
c) nome do produto mais barato."""

print('--mercadinho--')
tot = maisdmil = menor = cont = 0
barato = ' '

while True:
    produto = ' '
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    tot += preco
    cont += 1

    if preco > 1000:
        maisdmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    if resp == 'N':
        break


print(f'Produtos que custam mais de Mil reais: {maisdmil}')
print(f'Total gasto na compra: {tot}')
print(f'Produto mais barato: {barato}')
