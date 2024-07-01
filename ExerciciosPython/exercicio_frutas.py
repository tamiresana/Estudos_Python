
frutas = ['morango', 'uva', 'pera']

alergias = ['sono', 'coceira', 'espirro']

alergias.append(frutas[0])

for fruta in frutas:
  if fruta in alergias:
    print(fruta)

