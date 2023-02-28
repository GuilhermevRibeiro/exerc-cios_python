"""Crie um programa que leia o ano de nascimento de sete pessoas. No finalm mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores."""

atual = 2023
cont_maior = 0
cont_menor = 0
for pessoas in range(1, 8):
    nasci = int(input(f'Digite o ano de nascimento da {pessoas}º pessoa:'))
    idade = atual - nasci
    if idade > 17:
        cont_maior += 1
    else:
        cont_menor += 1

print(f'Dentro das 7 pessoas, temos {cont_maior} maiores de idade e {cont_menor} menores')
