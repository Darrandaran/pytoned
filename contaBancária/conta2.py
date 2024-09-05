from contaClass import ContaBancaria

conta1 = ContaBancaria(numero_conta="338438",titular="Melissa",saldo=1768)

print(conta1)
conta1.depositar(1500)
conta1.sacar(1500)
print(conta1.consultar_saldo())