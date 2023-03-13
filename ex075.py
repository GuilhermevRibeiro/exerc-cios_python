"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os números pares."""

num = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite mais outro número: ')),
       int(input('Digite o último número: ')))
if 9 in num:
    print(f'O número 9 aparece {num.count(9)} vezes')
else:
    print('O valor 9 não foi digitado')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')


