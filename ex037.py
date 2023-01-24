"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolhr qualserá a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal"""

numero = int(input('Digite um número inteiro: '))
op = int(input("""Escolha para qual base você quer converter o número:
[1] para binário
[2] para octal 
[3] para hexadecimal
escolha:"""))

if op == 1:
    print(f'A conversão de {numero} para binário é {bin(numero)}')
elif op == 2:
    print(f'A conversão de {numero} para octal é {oct(numero)}')
else:
    print(f'A conversão de {numero} para hexadecimal é {hex(numero)}')
