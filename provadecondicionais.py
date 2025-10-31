#Resposta
horas_trabalhadas = float(input("Digite o total de horas trabalhadas na semana: "))


valor_hora = float(input("Digite o valor da hora normal: R$ "))


jornada = 44


if horas_trabalhadas > jornada:
    horas_extras = horas_trabalhadas - jornada
    valor_hora_extra = valor_hora * 1.5
    print(f"\nResultado:")
    print(f"{horas_extras:.0f} horas extras a R$ {valor_hora_extra:.2f} cada.")
else:
    print("\nA jornada foi cumprida corretamente, sem horas extras.")