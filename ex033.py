#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

menor_num = num1
if num2<num1 and num2<num3:
    menor_num = num2
if num3<num1 and num3<num2:
    menor_num = num3

maior_num = num1
if num2>num1 and num2>num3:
    maior_num = num2
if num3>num1 and num3>num2:
    maior_num = num3

print(f'O menor número é {menor_num} e o maior é {maior_num}')