#MÉTODOS COM A STRING
#inicial =  "   fabricio CARRaro da ALuRa    "
#final = "FABRICIO CARRARO DA ALURA"

texto = "   fabricio CARRaro da ALuRa    "
print(texto)


#Metodo lower (Tudo em minusculo)
print(texto.lower())

#Metodo upper (Tudo maiusculo)
print(texto.upper())

#Metodo Strip (Remover espaços)
print(texto.strip())

#Metodo replace (troca de algum dado)
print(texto.replace("  ", " "))


#Juntando tudo
print(texto.strip().upper().replace("  ", " "))
