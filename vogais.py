palavra = input('Digite uma palavra para descobrir suas vogais: ')
vogais = 'aeiou'

contador = 0

for i in palavra:
  if i in vogais:
    contador += 1
    print(f'A {palavra} tem {contador} vogais')

    