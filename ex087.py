"""Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
som_par = maior = som_col = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            som_par += matriz[l][c]
    print()
print(f'A soma dos números pares é: {som_par}')
for l in range(0, 3):
    som_col += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {som_col}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')