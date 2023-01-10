"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
nome deles e escrevendo o nome do escolhido. """
import random

al1 = input('Nome do primeiro aluno: ')
al2 = input('Nome do segundo aluno: ')
al3 = input('Nome do terceiro aluno: ')
al4 = input('Nome do quarto aluno: ')

lista_alunos = [al1, al2, al3, al4]
sorteio = random.choice(lista_alunos)
print(f'O aluno sorteado para apagar o quadro foi: {sorteio}')