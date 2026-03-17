import csv

arquivo = "vendas-anuais-de-oleo-diesel-por-municipio.csv"

estadoEscolhido = input("Digite o estado (UF): ").upper()

anos = []
consumo = []

vendasPorAno = {}

with open(arquivo, "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    next(leitor)

    for linha in leitor:

        ano = int(linha[0])
        uf = linha[2]
        vendas = float(linha[6])

        if uf == estadoEscolhido:

            if ano not in vendasPorAno:
                vendasPorAno[ano] = 0

            vendasPorAno[ano] += vendas


for ano in sorted(vendasPorAno):

    anos.append(ano)
    consumo.append(vendasPorAno[ano])


def regressaoLinear(x, y):

    n = len(x)

    somaX = sum(x)
    somaY = sum(y)

    somaXY = 0
    somaX2 = 0

    for i in range(n):
        somaXY += x[i] * y[i]
        somaX2 += x[i] * x[i]

    b = (n * somaXY - somaX * somaY) / (n * somaX2 - somaX ** 2)
    a = (somaY - b * somaX) / n

    return a, b


a, b = regressaoLinear(anos, consumo)

print("\nModelo encontrado:")
print("Consumo =", a, "+", b, "* Ano")

print("\nPrevisão para próximos anos:")

ultimoAno = max(anos)

for i in range(1, 4):

    anoFuturo = ultimoAno + i
    previsao = a + b * anoFuturo

    print(anoFuturo, "->", int(previsao), "litros")