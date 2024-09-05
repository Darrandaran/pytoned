n1 = int(input("Insira um número:"))
if n1 >= 0:
    produto = 1
    if n1 == 0:
        print(f"0! = 1")
    else:
        for i in range(1,n1+1):
            print(produto)
            produto *= i
        
        print(f"!{n1}={produto}")
else:
    print("Entrada inválida")