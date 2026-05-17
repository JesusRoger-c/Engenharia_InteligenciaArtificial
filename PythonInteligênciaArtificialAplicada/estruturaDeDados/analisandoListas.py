

list_nomes = [
    "Gabriel Almeida",
    "Beatriz Costa",
    "Matheus Rodrigues",
    "Larissa Martins",
    "Felipe Gomes",
    "Camila Ribeiro",
    "Rafael Carvalho",
    "Juliana Barbosa",
    "Thiago Moreira",
    "Amanda Fernandes"
]

print(len(list_nomes))


#Adicionar mais valor na lista
list_nomes.append("Gabriel Almeida")
print(list_nomes)

#Juntar listas
list_nomes.extend(["Beatriz Costa", "Miguel Rian", "Pedro Augusto"])
print(list_nomes)


#Remover Elementos de uma lista
list_nomes.remove("Gabriel Almeida")
list_nomes.remove("Beatriz Costa")
print(list_nomes)