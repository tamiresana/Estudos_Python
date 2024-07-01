'''soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))

    soma = soma + nota

print(soma / 3)'''

# Slices
lista = [1, 5, 6, 3, 6, 8, 9]
print(lista[0:3])
print(lista[3:6])# intervalo do 3 até antes do 6
print(lista[3:]) # intervalo 3 até o fim da lista
print(lista[-1])# ultimo da lista
print(lista[3:6:2])# o 2 pula de 2 em 2

lista2 = [1, 2, 3]

lista.append(3) #append sempre no final eu adiciono algo
lista.insert(2, 10) #insert escolho qual indice e depois o elemento que vou inserir
lista.extend(lista2) #pega os elementos de uma lista e insere no final da outra lista (concatenar)
lista.pop() #elimina o ultimo elemento se eu não especifico
lista.remove(3) #diz o valor que eu quero excluir. não é o indice e sim elemento(obs ele remove o primeniro elemento que elçe encntra caso tenha repetido)
lista.index(2) #diz qual o indece do elemento x
lista.count(2) #diz quantas vezes aparece o elemento x
lista.sort() #ordena a lista de forma crescente - Decrescente: lista.sort(reverse=True)



#Funções
#print(len(lista)) - sum - max - min

