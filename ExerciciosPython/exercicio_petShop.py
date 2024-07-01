# Solicitar ao usuário o nome do cachorro
nome_cachorro = input("Digite o nome do cachorro: ")

# Solicitar ao usuário a idade humana do pet
idade = int(input("Digite a idade humana do pet (um número inteiro): "))

# Calcular a idade do pet em anos de cachorro
idade_pet = idade + 7

# Solicitar ao usuário o porte do cachorro
porte_cachorro = input("Informe o porte do seu cachorro (ex.: 'Grande', 'Médio' ou 'Pequeno'): ").capitalize()

# Lista de portes válidos
portes = ["Grande", "Médio", "Pequeno"]

# Solicitar ao usuário o total de banhos até agora
total_banho = int(input("Informe o total de banhos até agora: "))

# Definindo os custos e valores dos banhos por porte de cachorro
custo_grande = 20
custo_medio = 15
custo_pequeno = 5
banho_grande = 75
banho_medio = 60
banho_pequeno = 50


# Exibir a idade do pet
print(f"A idade do seu pet é {idade_pet} anos")

# Calcular o lucro com base no porte do cachorro
if porte_cachorro == "Grande":
        total_anual = (banho_grande * total_banho) - (custo_grande  * total_banho)

elif porte_cachorro == "Médio":
        total_anual  = (banho_medio * total_banho) - (custo_medio  * total_banho)

elif porte_cachorro == "Pequeno":
        total_anual = (banho_pequeno * total_banho) - (custo_pequeno * total_banho)
else:
    print("Porte não existente!")
    total_anual = None

# Verificar se o porte do cachorro é válido para exibir o lucro
if total_anual is not None:
    print(f"Olá, {nome_cachorro} tem {idade_pet} anos e nos últimos 12 meses o lucro com este animal foi de R${total_anual:.2f}")   