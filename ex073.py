"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do brasileirão, na ordem de colocação.
Depois mostre:
a) Os 5 primeiros
b) Os últimos 4 colocados
c) Times em ordem alfabética
d) Em que posição está o time do Chapecoense"""

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atletico-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletic-PR', 'Cuiabá', 'Juventude', 'Grêmio',
         'Bahia', 'Sport', 'Chapecoense')

print('=' * 23)
print('TABELA BRASILEIRÃO 2021')
print('=' * 23)

print(f'Os 5 primeiros colocados do Brasileirão de 2021 foram: {times[0:6]}')
print('=-' * 48)
print(f'Os últimos 4 colocados do Brasileirão de 2021 foram: {times[-4:]}')
print('=-' * 48)
print(f'O time da Chapecoense terminou o Brasileirão em {times.index("Chapecoense")+1}º lugar')
print('=-' * 48)
print(f'Times em ordem alfabética: {sorted(times)}')
