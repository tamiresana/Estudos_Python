
#for i in range(1, 11):
#  if i % 2 == 0:
#    print(i)

numero = int(input('Digite um numero para ver a tabuada: '))

print(f'Tabuada do {numero}')

for i in range(1, 11):
  resultado = numero * i
  print(f'{numero} x {i} = {resultado}')

#for i in range(1, 11, 2): o ultimo numero quer dizer que vai pular de 2 em 2
#  if i % 2 == 0:
#    print(i)