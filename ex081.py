"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a)Quantos números foram digitados.
b)A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista."""

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    if resp == 'N':
        break

print(f'A lista de números digitadas é {lista}')
print('-' * 20)
print(f'Foram digitados {len(lista)} valores')
print('-' * 20)
print(f'A ordem da lista em forma crescente é {sorted(lista)}')
print('-' * 20)
lista.sort(reverse=True)
print(f'A ordem da lista em forma decrescente é {lista}')
print('-' * 20)
if 5 in lista:
    print('O número 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')