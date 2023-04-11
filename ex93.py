"""Crie um programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gools feitos durante o campeonato."""

dados = {}
partidas = []
dados['Nome'] = str(input('Nome: '))
tot = int(input(f'Quantas partidas {dados["Nome"]} jogou? :'))
for c in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partida {c+1}? :')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

