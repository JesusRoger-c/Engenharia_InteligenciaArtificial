print("========= Menu ===========")
print("[1] Hambúrguer: R$ 12,00")
print("[2] Batata frita: R$ 7,00")
print("[3] Refrigerante: R$ 5,00")

# preços
preco_hamburguer = 12
preco_batata = 7
preco_refrigerante = 5

# quantidades
qtd_hamburguer = int(input("Quantos hambúrgueres? "))
qtd_batata = int(input("Quantas batatas fritas? "))
qtd_refrigerante = int(input("Quantos refrigerantes? "))

# cálculo
total = (qtd_hamburguer * preco_hamburguer) + \
        (qtd_batata * preco_batata) + \
        (qtd_refrigerante * preco_refrigerante)

# saída
print("\n===== RESUMO DO PEDIDO =====")
print(f"Hambúrguer: {qtd_hamburguer} x R$12 = R${qtd_hamburguer * preco_hamburguer}")
print(f"Batata: {qtd_batata} x R$7 = R${qtd_batata * preco_batata}")
print(f"Refrigerante: {qtd_refrigerante} x R$5 = R${qtd_refrigerante * preco_refrigerante}")
print(f"TOTAL: R${total}")