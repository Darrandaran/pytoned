n1 = int(input("Insira um número: "))

if n1 <=1:
    print(f"{n1} não é primo")
else:
    for i in range(2, n1):
        if n1 % i == 0:
            print(f"{n1} não é um número primo.")
            break
    print(f"{n1} é um número primo")