 Previsão de Consumo de Diesel no Brasil

 Projeto acadêmico desenvolvido para a disciplina **Processamento da Informação** — UFABC (Universidade Federal do ABC)

---

Visão Geral

Este projeto em **Python** analisa o consumo histórico de óleo diesel por estado brasileiro, utilizando **regressão linear simples** para projetar o consumo dos próximos 3 anos.

O programa lê um arquivo CSV com dados de vendas por município, filtra pelo estado escolhido pelo usuário, agrega o consumo por ano e constrói um modelo matemático de previsão.

---

Objetivo

Simular um cenário de **planejamento logístico de combustível**, onde é necessário prever a demanda antes que ela aconteça — auxiliando na tomada de decisões sobre produção e distribuição.

---

Etapas de Execução

1. Entrada de Dados
O usuário informa a sigla de um estado (UF), convertida automaticamente para maiúsculas.

2. Leitura do CSV
O programa abre `vendas-anuais-de-oleo-diesel-por-municipio.csv` e extrai:
| Coluna | Campo |
|--------|-------|
| 0 | Ano |
| 2 | UF do município |
| 6 | Volume de vendas |

Apenas linhas do estado informado são consideradas.

3. Agregação por Ano
As vendas de todos os municípios do estado são somadas ano a ano, formando um dicionário `vendasPorAno`.

4. Regressão Linear
A função `regressaoLinear(x, y)` calcula os coeficientes da reta pelo **método dos mínimos quadrados**:
```
Consumo = a + b × Ano
```

- **a** → intercepto (valor base)
- **b** → inclinação (variação média por ano)

5. Saída
O programa exibe os coeficientes do modelo e a previsão para os **3 anos seguintes** ao último ano presente nos dados.

---

Exemplo de Saída
```
Modelo encontrado:
Consumo = -9876543210.5 + 4950000.0 * Ano

Previsão para próximos anos:
2024 -> 1234567890 litros
2025 -> 1239517890 litros
2026 -> 1244467890 litros
```

---

Como Executar
```bash
python previsao_diesel.py
```

Quando solicitado, informe a sigla do estado (ex: `SP`, `RJ`, `MG`).

---

Tecnologias Utilizadas

- Python
- Leitura de arquivos CSV
- Estruturas básicas de programação
- Regressão linear simples (implementação manual)

---

Fonte dos Dados

Dados públicos da **ANP – Agência Nacional do Petróleo, Gás Natural e Biocombustíveis**.

---

Diagrama Funcional

![Diagrama Funcional - Previsão de Consumo de Diesel](https://github.com/user-attachments/assets/1b81b698-0adb-4051-8db3-83ae095b59c9)

---


Projeto acadêmico — Processamento da Informação · UFABC

Descrição Funcional do Projeto 2

Billings — Monitoramento Participativo da Qualidade da Água

Contexto e Justificativa
A Represa Billings, localizada na região do ABC Paulista, é um dos maiores reservatórios de água doce da América Latina e está diretamente relacionada ao território de atuação deste projeto. Responsável pelo abastecimento de milhares de pessoas, a Billings enfrenta sérios desafios de poluição, degradação ambiental e pressão urbana, tornando urgente o desenvolvimento de iniciativas que promovam a conscientização, o monitoramento e a preservação desse recurso hídrico essencial.

Objetivos
Promover o acompanhamento contínuo da qualidade da água da Represa Billings;

ODS
🔵 ODS 6 Água Potável e Saneamento - Monitoramento da qualidade e acesso seguro à água
🟢 ODS 15 Vida Terrestre - Preservação do ecossistema do entorno da represa

Descrição Funcional
O projeto propõe o desenvolvimento de um programa digital de monitoramento participativo, com as seguintes funcionalidades principais:
1. Ferramenta de pesquisa de Qualidade da Água, exibição de indicadores ambientais da Represa Billings em tempo real, como nível de turbidez, pH e índice de oxigenação.
2. Histórico e Tendências Módulo de visualização de dados históricos, permitindo identificar padrões de degradação ou melhora da qualidade da água ao longo do tempo.

Público-Alvo
Pesquisadores ambientais - Ferramenta 


