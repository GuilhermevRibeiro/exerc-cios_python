"""Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
 tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""
import random
numero = random.randint(0, 10)
tentativa = 0
print('Vou pensar num número entre 0 e 10, tente adivinhar!')
acertou = False

while not acertou:
    usuario = int(input('Em qual número você acha que eu pensei: '))
    tentativa += 1
    if usuario == numero:
        acertou = True
    else:
        if usuario < numero:
            print('mais... tente mais uma vez.')
        elif usuario > numero:
            print('menos... tente mais uma vez')

print(f'Parabéns! você acertou em {tentativa} tentativas')