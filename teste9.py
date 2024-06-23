compra = float(input('Digite o valor da sua compra: '))


if compra >= 500:
  print('PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%')
  compra_desconto = compra - (compra * 0.30)
  print(f'O valor da compra é {compra_desconto}')
elif compra >= 250:
  print('PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00')
  compra_desconto = compra - (compra * 0.10)
  print(f'O valor da compra é {compra_desconto}')
else:
  print('POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.')