idade = int(input("sua idade é: "))
if idade >=18 and idade<65:
    print ("você é adulto")
elif idade >= 65:
    print ("você é idoso")
elif idade >12 and idade <18:
    print ("você é adolescente")
else:
    print ("você é criança")