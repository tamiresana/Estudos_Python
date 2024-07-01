palavra = input('Digite uma palavra para descobrir suas vogais: ')
vogais = ['a', 'e', 'i', 'o', 'u']
contador = 0

for letra in palavra:
  if letra in vogais:
    print(f'Contém a letra {letra}')
    contador += 1

 #Imprima o número total de vogais na palavra

print(f'O total de vogais na palavra é {contador}')   

    