num1 = int(input("insira um número: "))
total = 0
divisor = 1
while divisor < num1:
    if num1 % divisor == 0:
        total += divisor
    divisor += 1
if total == num1:
    print ("correto")
else:
    print ("incorreto")
