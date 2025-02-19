Largura_Garagem=float(input("Entre com a Largura da garagem em metros "))
Profundidade_Garagem=float(input("Entre com a Profundidade garagem em metros "))

#calcular Área da Garagem
Area_Garagem=Largura_Garagem * Profundidade_Garagem

Largura_Terreno=float(input("Entre com a Largura do Terreno em metros "))
Profundidade_Terreno=float(input("Entre com a Profundidade do Terreno em metros "))

#Calcular Área do Terreno
Area_Terreno=Largura_Terreno * Profundidade_Terreno

#Calcula porcentual da ocupação
Percentual_Ocupacao=(Area_Garagem / Area_Terreno)*100

print('Resultado área terreno: ', Area_Terreno)
print('Resultado área garagem: ', Area_Garagem)
print("#############################################")
print('Percentual da ocupação', Percentual_Ocupacao)