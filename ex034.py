"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Digite seu salário atual: '))

if salario > 1250:
    print(f'Seu aumento será de 10%, a partir de agora você ganha: R${salario*1.10:.2f}')
else:
    print(f'Seu aumento será de 15%, a partir de agora você ganha: R${salario*1.15}')