"""Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador."""

"""Crie um programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gools feitos durante o campeonato."""
time = []
dados = {}
partidas = []

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {dados["Nome"]} jogou? :'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c+1}? :')))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro. Responda apenas S ou N')
    if resp == 'N':
        break
print()
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, não existge jogador com código {busca}')
    else:
        print(f'--Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')

