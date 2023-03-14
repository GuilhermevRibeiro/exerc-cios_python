"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas."""

lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    if num % 2 == 0:
        lista_par.append(num)
    elif num % 2 == 1:
        lista_impar.append(num)

    if resp == 'N':
        break

print(f'A lista com todos os números é {lista}')
print('-' *30)
print(f'A lista com os números pares é {lista_par}')
print('-' *30)
print(f'A lista com os números ímpares é {lista_impar}')
print('-' *30)