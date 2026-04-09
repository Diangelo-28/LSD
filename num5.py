hora_atual = int(input("hora atual: "))
espera = int(input("horas de espera: "))
alarme = (hora_atual + espera) % 24
print (f"O alarme irá tocar ás {alarme} ")