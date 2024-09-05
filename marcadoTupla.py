def main():
    produtos = [('Beringela',5.0),("Mirtilo",9.0),("Morango",7.0),("Cereja",12.79),("Bergamota",2.45),("Maracujá",12.98),("Pera",6.0),("Banana",3.24),("Carambola",5.60)]
    descontoValor = 10 
    descontoPorc = 20
    soma = 0

    for produto in produtos:
        soma += produto[1]
    
    if soma > descontoValor:
        print(f" Valor total com desconto é {round(soma*(100-descontoPorc)/100,2)}")
    else:
        print(f"Valor total é {soma}")
if __name__ == "__main__":
    main()