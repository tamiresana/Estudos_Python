nome = "Paula Martins"
mes = "Janeiro"
valor = "R$500,00"
desconto = "10%"
cupom = "PAULAÉ10"


print(f"Olá, {nome} .Em {mes} você realizou uma compra no valor de {valor} e ganhou um desconto de {desconto} em sua próxima compra. Use o cupom {cupom}.")

#Formas de usar o Format

format_1 = f"O nome da pessoa é {nome}, desconto dela é {desconto}"
format_2 = "O nome da pessoa é {}, desconto dela é {}".format(nome, desconto)
format_3 = "O nome da pessoa é {a}, desconto dela é {b}".format(a=nome,b=desconto)