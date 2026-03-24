import csv
import numpy as np  # Importando as bibliotecas essenciais para computação científica, álgebra linear e leitura dos dados

# Definição da fonte de dados (extraídos da ANP)
arquivo = "vendas-anuais-de-oleo-diesel-por-municipio.csv"
estadoEscolhido = input("Digite o estado (UF): ").upper()

# Dicionário para acumular as vendas totais por ano (agregação de dados)
vendasPorAno = {}

# Abertura e leitura do arquivo CSV com tratamento de codificação
with open(arquivo, "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    next(leitor)  # Pula o cabeçalho para evitar erros de conversão de tipo

    for linha in leitor:
        # Extração de colunas específicas: [0] Ano, [2] UF, [6] Volume
        ano = int(linha[0])
        uf = linha[2]
        vendas = float(linha[6])

        # Filtragem condicional: processa apenas os dados da UF selecionada
        if uf == estadoEscolhido:
            # O método .get() inicializa o ano com 0 caso ele ainda não exista no dicionário
            vendasPorAno[ano] = vendasPorAno.get(ano, 0) + vendas

# Vetorização: Transforma os dados em arrays NumPy para permitir cálculos matemáticos eficientes
anos = np.array(sorted(vendasPorAno.keys()))
consumo = np.array([vendasPorAno[a] for a in anos])

# polyfit realiza a Regressão Linear pelo Método dos Mínimos Quadrados.
# O parâmetro '1' define um modelo de primeiro grau (reta: y = bx + a).
# b representa a inclinação (tendência anual) e 'a' o intercepto (valor base).
b, a = np.polyfit(anos, consumo, 1)

print(f"\nModelo matemático encontrado (via NumPy):")
print(f"Equação: Consumo = {a:.2f} + {b:.2f} * Ano")

print("\nPrevisão para o próximo triênio:")
ultimoAno = anos.max()

# Loop de simulação para projeção de demanda futura
for i in range(1, 4):
    anoFuturo = ultimoAno + i
    # Aplicação da função linear encontrada para estimar o consumo futuro
    previsao = b * anoFuturo + a
    print(f"{anoFuturo} -> {int(previsao)} litros")
  

