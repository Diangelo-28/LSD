total = 0
num1 = int(input("insira um número: "))
while num1 != 0:
    print ("tente novamente")
    total =   total +  num1
    num1 = int(input("insira um número: "))
print (f"número correto é: {num1}, a soma das tentativas foi {total}")