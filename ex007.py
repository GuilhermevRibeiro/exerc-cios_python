#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
média = (nota1+nota2)/2
print(f'A média do aluno é igual a: {média:.1f}')