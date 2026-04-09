import random
tentativas = 3
while tentativas > 0 :
    num1 = int(input("selecione um número entre 1 e 10: "))
    num2 = random.randint(1,10)
    if num1 == num2:
        print ("resposta correta")
        break
    else:
        print ("resposta incorreta")
        tentativas -= 1
    if tentativas == 0:
        print ("tentativas excedidas, você perdeu")