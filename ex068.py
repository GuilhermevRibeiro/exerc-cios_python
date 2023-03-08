"""Faça um programa que jogue par ou ímpar com o computador. O jogo só sera interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
import random
print('Vamos jogar par ou ímpar, escolha qual você quer e logo em seguida seu número!')
print('-' *78)
cont = 0
while True:
    jogador = int(input('Digite 1 para PAR e 2 para ÍMPAR: '))
    escolha = int(input('Digite um número de 0 a 10: '))
    computador = random.randint(0, 10)
    som = escolha+computador
    if jogador == 1:
        print(f'Você escolheu {escolha} e eu escolhi {computador}, totalizando {som}')
        if som % 2 == 0:
            print('Você ganhou!')
            cont += 1
        else:
            print('você perdeu!')
            break
    elif jogador == 2:
        print(f'Você escolheu {escolha} e eu escolhi {computador}, totalizando {som}')
        if som % 2 == 1:
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    else:
        break
if cont == 1:
    print('Fim de jogo! Você ganhou apenas uma vez')
elif cont > 1:
    print(f'Fim de jogo, você ganhou {cont} vezes')
else:
    print('Fim de jogo.')
