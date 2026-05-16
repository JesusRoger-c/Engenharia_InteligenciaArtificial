#LISTAS
lista_de_nomes = [
    "João Silva",
    "Maria Oliveira",
    "Pedro Santos",
    "Ana Souza",
    "Carlos Ferreira"
]


lista_de_medias = [
    8.9,
    2.6,
    8.4,
    3.6,
    9.9
]

#print(lista_de_nomes)
#print(lista_de_medias)

n = 0
while n < 5:
     lista_de_medias[n] = lista_de_medias[n] + 1.0
     if lista_de_medias[n] > 10.0:
        lista_de_medias[n] = 10.0

     n = n + 1


print(lista_de_medias)



