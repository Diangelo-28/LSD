preço = float(input("preço: "))
quantidade = int(input("quantidade: "))
desconto = preço * 0.35
frete = 4 + (quantidade - 1) * 0.8
total =  (preço - desconto) * quantidade + frete
print (f"O custo total será{total}")