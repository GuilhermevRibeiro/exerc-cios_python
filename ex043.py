"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela:
-Abaixo de 18.5: abaixo do peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida"""

peso = float(input('Diga quanto você pesa: '))
altura = float(input('Diga sua altura: '))
imc = peso / (altura*altura)

if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal')
elif 25 <= imc < 30:
    print('Você está no sobrepeso')
elif 30 <= imc < 40:
    print('Você está obeso')
else:
    print('Você está em obesidade mórbida')