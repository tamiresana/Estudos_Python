nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite sua idade: "))

print(type(idade))  # Apenas para verificar o tipo de dado
print(type(altura))  # Apenas para verificar o tipo de dado

if type(idade) != int:
  print("Digite um número válido!")
if type(altura) != float:
  print("Digite um número válido!")

print(f"O nome do usuario é {nome}, sua altura em metros é {altura}, e sua idade é {idade} anos.")