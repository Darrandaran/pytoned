def main():
    # Despesas e seus custos
    despesas = (("Academia",450.34),("Farmácia",34.67),("Alimentação",450.34),("Hospital",589.23),("Parcela do cartão",20.45),("Internet",120))
    # Valor total
    total = 0
    # Lista de despesas
    print("Despesa | Valor\n_____________________")
    for despesa in despesas:
        print(f"{despesa[0]}   R$ {despesa[1]}")
        # Calcula o total
        total += despesa[1]
    # Mostra o total das despesas
    print(f"___________________\nTotal: R$ {total}")
if __name__ == "__main__":
    main()