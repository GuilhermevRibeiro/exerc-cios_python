"""Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal, e condição
de pagamento:
-Á vista dinheiro/cheque: 10% de desconto
-Á vista no cartão: 5% de desconto
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros"""

compra = float(input('Qual o valor da compra: R$'))

print("""Qual a forma de pagamento
[1] dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão""")

pag = int(input('Forma de pagamento: '))

if pag == 1:
    print(f'O valor da compra é R${compra*0.90:.2f}')
elif pag == 2:
    print(f'O valor da compra é R${compra*0.95:.2f}')
elif pag == 3:
    print(f'O valor da compra é em duas vezes de R${compra/2:.2f}')
elif pag == 4:
    qtd_parcela = int(input('Em quantas parcelas você pretende pagar? '))
    print(f"O valor da sua compra será em {qtd_parcela} vezes de R${(compra * 1.20) / qtd_parcela :.2f}")
