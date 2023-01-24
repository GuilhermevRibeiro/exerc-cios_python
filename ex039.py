"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deve
mostrar o tempo que falta ou que passou do prazo."""

nascimento = int(input('Qual seu ano de nascimento: '))
idade = 2023 - nascimento

print(f'Você tem {idade} anos')

if (2023-nascimento) < 18:
    print(f'Você ainda é menor de idade, e deverá se alistar daqui {2023-idade} anos')
elif (2023-idade) == 18:
    print(f'Quem nasceu em {idade} tem 18 anos em 2023, você precisa se alistar.')
else:

    print(f'Você já devia ter se alistado há {idade - 18} anos')