"""Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas e minúsculas.
-Quantas letras ao todo sem o espaço.
-Quantas letrar tem o primeiro nome. """

nome = str(input('Digite seu nome: ')).strip()

print(f'Seu nome só com letras maiúsculas é: {nome.upper()} ')
print(f'Seu nome só com letras minúsculas é: {nome.lower()}')
print(f'Seu nome tem ato todo {len(nome)-nome.count(" ")} letras.')
nome_separado = nome.split()
print(f'Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras')