print('Analisando um triângulo')
v1 = float(input('Primeira reta: '))
v2 = float(input('Segunda reta: '))
v3 = float(input('Terceira reta: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')