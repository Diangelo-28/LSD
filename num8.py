while True:
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("insira o segundo número: "))
    opc = input("selecione a operação (+ - * / ): ")
    if opc == "+":
        print (num1 + num2)
    elif opc == "-":
        print (num1 - num2)
    elif opc == "*":
        print (num1 * num2)
    elif opc == "/":
        print (num1 / num2)
    fim = input("deseja encerrar?: ")
    if fim == "sim":
        break
    