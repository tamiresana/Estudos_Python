for i in range(5): # Usado quando o número de iterações é conhecido previamente.
    print(i)
print("-----------------------------")
i = 0
while i <5: # Usado quando o número de iterações não é conhecido previamente e depende de uma condição ser verdadeira.
    print(i)
    i += 1
print("-----------------------------")

lista_frutas = ['maçã', 'banana', 'laranja']
for fruta in lista_frutas:
    print(fruta)

# Exemplo usando enumerate()
for indice, valor in enumerate(lista_frutas):
    print(f"Índice {indice}: {valor}")

# Exemplo usando zip()
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
for num, letra in zip(numeros, letras):
    print(num, letra)

print("-----------------------------")
senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input('Digite a senha: ')
print('Senha correta!')