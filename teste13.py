
#for i in range(1, 11):
#  if i % 2 == 0:
#    print(i)

numero = int(input('Digite um numero para ver a tabuada: '))

print(f'Tabuada do {numero}')

for i in range(1, 11):
  resultado = numero * i
  print(f'{numero} x {i} = {resultado}')