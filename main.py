import requests  # Importa a biblioteca requests, que permite fazer requisições HTTP

# Define a URL do endpoint da API do IBGE para obter todos os municípios do estado de São Paulo (código 35)
url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios"

# Faz uma requisição GET para a URL especificada
response = requests.get(url)

# Converte a resposta JSON em um objeto Python (lista de dicionários)
municipios = response.json()

# Todos os municípios retornados na lista
for municipio in municipios:
    print(municipio["nome"])  # Imprime o nome de cada município
