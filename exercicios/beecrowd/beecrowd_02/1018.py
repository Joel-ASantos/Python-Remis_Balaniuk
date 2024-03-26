try:
    money = int(input())
    cedulas = [100,50,20,10,5,2,1]

    print(money)
    for index in cedulas:
        qtd = money // index
        money %= index
        print(f"{qtd} nota(s) de R$ {index},00")
except ValueError:
    print("Presentation Error")