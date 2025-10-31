salario = float(input("Digite o salário mensal: R$ "))
meses_trabalhados = int(input("Digite o número de meses trabalhados: "))


ferias_proporcionais = (salario / 12) * meses_trabalhados


print(f"\nFérias proporcionais de R$ {ferias_proporcionais:.2f}")