"""Crie um programa que leia dois valores e mostre um menu com opções de somar, multiplicar, maior, novos números e
sair do programa. Seu programa deverá realizar a operação solicitada em cada caso."""
pri_valor = int(input('Primeiro valor: '))
seg_valor = int(input('Segundo valor: '))
resposta = 0
while resposta != 5:
    print("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    """)
    resposta = int(input('Qual é a sua opção: '))

    if resposta == 1:
        soma = pri_valor + seg_valor
        print(f'A soma dos dois valores é {soma}')

    elif resposta == 2:
        produto = pri_valor * seg_valor
        print(f'A multiplicação dos dois valores é: {produto}')

    elif resposta == 3:
        if pri_valor > seg_valor:
            print(f'O primeiro valor é maior que o segundo, pois {pri_valor} > {seg_valor}.')
        else:
            print(f'O segundo valor é maior que o primeiro, pois {seg_valor} > {pri_valor}')

    elif resposta == 4:
        pri_valor = int(input('Digite um novo número para o primeiro valor'))
        seg_valor = int(input('Digite um novo número para o segundo valor'))

    elif resposta == 5:
        print('finalizando')

    else:
        print('Resposta inválida')

print('Fim do programa')

