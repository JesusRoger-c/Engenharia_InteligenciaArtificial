entrega = float(input("Quantos km são? "))
print("1 - Está chovendo\n2 - Não está chovendo")
chuva = int(input("Está chovendo? "))

# Define taxa base
if entrega <= 5:
    taxa = 5
elif entrega <= 10:
    taxa = 8
else:
    taxa = 10

# Adicional de chuva
if chuva == 1:
    taxa += 2

print(f"Valor final da entrega: R$ {taxa}")