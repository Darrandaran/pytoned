limite_velocidade = 120
velocidade_usuario = float(input ("digite a velocidade do carro: "))

if velocidade_usuario > limite_velocidade:
    print("voce esta acima do limite, reduza para menos de", limite_velocidade, "km/h")

    excesso_velocidade = velocidade_usuario - limite_velocidade

    print("voce esta", excesso_velocidade, "km/h acima do limite")

else:
    print("velocidade dentro do limite")