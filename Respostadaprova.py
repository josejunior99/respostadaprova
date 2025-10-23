tempo = float(input("Tempo de serviço em anos (ex: 2 ou 1.5): "))
saldo_fgts = float(input("Saldo do FGTS em reais (ex: 10000): "))

if tempo > 1:
    multa = 0.4 * saldo_fgts
else:
    multa = 0.0

if multa > 0:
    print(f"Resultado: multa = R$ {multa:,.2f}")
else:
    print("Resultado: não há multa (tempo ≤ 1 ano).")
