"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços. Na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular."""

lista = ('Lápis', 1.20,
         'Borracha', 1.50,
         'Caderno', 10.00,
         'Estojo', 25.55,
         'Transferidor', 5.50,
         'Compasso', 8.75,
         'Mochila', 75.99,
         'Canetas', 15.99,
         'Livro', 120.25)

print('~' *30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('~' *30)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('~' *30)