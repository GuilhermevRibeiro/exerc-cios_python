"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
-Até 9 anos: mirim
-Até 14 anos: infantil
-Até 19 anos: junior
-até 25 anos: sênior
-Acima: Master"""

nascimento = int(input('Ano de nascimento: '))
idade = 2023 - nascimento
print(f'O atleta tem {idade} anos')

if idade <= 9:
    print('O atleta se encaixa na categoria mirim')
elif idade <= 14:
    print('O atleta se encaixa na categoria infantil')
elif idade <= 19:
    print('O aluno se encaixa na categoria junior')
elif idade <= 25:
    print('O atleta se encaixa na categoria sênior')
else:
    print('O atleta se encaixa na categoria master')

