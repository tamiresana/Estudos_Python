import requests

#Defina o CEP que você quer consultar

cep = '01001000'

#Faça a requisição para o serviço ViaCEP

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

#Verifique se a requisição foi bem sucedida
if response.status_code == 200:
  data = response.json() # Converta a resposta para um dicionário
  print(f'Localidade: {data['localidade']}\nCEP: {data['cep']}\nLogradouro: {data['logradouro']}') # Exiba os dados retornados

else:
  print(f'Erro ao fazer a requisição: {response.status_code}')