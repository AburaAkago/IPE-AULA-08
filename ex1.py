import os
os.system('cls')

estoqueFrutas1={'kiwis':430,'bananas':312,'laranjas':525,'peras':217}
print("conteúdo completo do dicionário (estoque) = ",estoqueFrutas1)
estoqueFrutas1['bananas']+=200
numItens=len(estoqueFrutas1)
print("Numero de itens = ",numItens)
print("estoque de bananas = ",estoqueFrutas1['bananas'])

print("Estoque total de frutas = ",estoqueFrutas1)