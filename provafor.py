
salario = float(input("Digite o valor do salário: R$ "))
dias_atraso = int(input("Digite o número de dias de atraso: "))


if dias_atraso > 5:
    multa_dia = salario * 0.02
    multa_total = multa_dia * dias_atraso
    print(f"\nMulta diária: R$ {multa_dia:.2f}")
    print(f"Valor total da multa: R$ {multa_total:.2f}")
else:
    print("\nNão há multa, o atraso foi de 5 dias ou menos.")