dicEstadoCapital = {"Rio de Janeiro":"Rio de Janeiro",
                    "São Paulo":"São Paulo",
                    "Minas Gerais":"Belo Horizonte",
                    "Bahia": "Salvador",
                    "Amazonas":"Manaus"}
print("A capiral de Rio de Janeiro é ",dicEstadoCapital["Rio de Janeiro"])
for chave in dicEstadoCapital:
    print("Listagem das chaves do dic Estado Capital = ",chave)
print("Lista de estados: \n",list(dicEstadoCapital.keys()))
print("Lista de estados: \n",list(dicEstadoCapital.values()))