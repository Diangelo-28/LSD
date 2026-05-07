import random
lista1 = []
lista2 = []
while True:
    login = input("Crie uma conta, digite um nome de usuário: ").lower().strip()
    if login == "":
        print("O usuário não pode estar em branco")
        continue
    senha = input("Agora crie uma senha: ").lower().strip()
    if senha == "":
        print("A senha não pode estar em branco")
        continue
    lista1.append(login)
    lista2.append(senha)
    print("Conta criada com sucesso")
    break
while True:
        login2 = input("Usuário: ").lower().strip()
        if login2 in lista1:
            abuble = lista1.index(login2)
            print("Usuário encontrado")
            senha2 = input("Senha: ").lower().strip()
            if senha2 == lista2[abuble]:
                print(f"Seja bem-vindo {login2}, aproveite o jogo")
                break
            else:
                print("Senha inválida!")
        else:
            print("Usuário não encontrado!")
while True:
    num1 = input("Eu quero jogar um jogo, você quer jogar? ").lower().strip()
    if num1 == "sim":
        print("Que os jogos comecem!")
        num2 = input("Selecione uma dificuldade:\n fácil (1-10)\n médio (1-50)\n difícil (1-100)").lower().strip()
        if num2 == "fácil":
                num3 = 10
        elif num2 == "médio":
                num3 = 50
        elif num2 == "difícil":
                num3 = 100
        else:
              print("Dificuldade inválida! Selecione fácil, médio ou difícil: ")
              continue
        num4 = random.randint(1, num3)
        while True:
                num5 = input(f"Escolha um número entre 1 e {num3}: ").strip()
                if num5.isdigit():
                        num6 = int(num5)
                        break
                else:
                        print("Inválido! Somente números inteiros positivos.")
        while num6 != num4:
                        if num6>num4:
                                print("Mais baixo, tá pensando muito alto")
                        elif num4>num6: 
                                print ("Mais alto, tá baixo ainda")
                        print("Errou meu querido, tente outra vez")
                        while True:
                                num5 = input("Digite outro número: ").strip()
                                if num5.isdigit():
                                        num6 = int(num5)
                                        break
                                else:
                                        print("Inválido! Somente números inteiros positivos.")
                        if num6 == num4:
                                print("Você acertou! Meus parábens Mário, favor não quebrar o código")
    elif num1 == "não":
        print ("Sniff sniff :(")
        break
    else:
        print ("Resposta inválida! Somente (sim) ou (não)\nVerifique se a grafia está correta")
       
        



            
