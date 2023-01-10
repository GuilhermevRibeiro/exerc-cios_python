"""Um professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome
dos quatro alunos e mostre a ordem sorteada"""

from random import shuffle

al1 = input('Nome do primeiro aluno: ')
al2 = input('Nome do segundo aluno: ')
al3 = input('Nome do terceiro aluno: ')
al4 = input('Nome do quarto aluno: ')

lista_alunos = [al1, al2, al3, al4]
shuffle(lista_alunos)
print('A ordem de apresentação dos alunos sera: ')
print(lista_alunos)