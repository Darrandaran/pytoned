class ContaBancaria:
    def __init__(self, numero_conta, titular, confianca = 1,status = True,saldo=0.0, limite=1000.0, limite_max = 1000.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        self.limite_atual = limite
        self.limite_max = limite_max
        self.status = status
        self.confianca = confianca

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def consultar_limite(self):
        return f"Limite atual: R${self.limite_atual}"

    def pagar(self,valor,forma_pagamento):
        fp = forma_pagamento
        if 0 <= valor:
            if fp == "db":
                if self.saldo >= valor:
                    self.saldo -= valor
                    return print("Pagamento realizado com sucesso")
                else:
                    return print("Saldo Insuficiente")
            elif fp == "cr":
                if self.limite_atual >= valor:
                    self.limite_atual -= valor
                    return print("Pagamento realizado com sucesso")
                else:
                    return print("Limite excidido")
            else:
                return print("ERRO")
        else:
            return "ERRO"
            
    def consultar_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

    def __str__(self):
        return f"Conta: {self.numero_conta}\nTitular: {self.titular}\nSaldo: R${self.saldo:.2f}"