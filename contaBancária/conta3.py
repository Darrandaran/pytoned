from contaClass import ContaBancaria

conta1 = ContaBancaria(numero_conta="783457",titular="luiza",saldo=0)

print (conta1)

conta1.depositar(2000)

print(conta1.consultar_saldo())

conta1.sacar(350)

print(conta1.consultar_saldo())

print(conta1.consultar_limite())
