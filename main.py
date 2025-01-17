import pandas as pd  # importando a biblioteca pandas


tabela = pd.read_csv('cancelamentos.csv')  # importando os dados

# Passo 2: Visualizar os dados (entender a base + identificar problemas)
print(tabela)

# Passo 3: Descartar os dados que não são úteis para minha resolução

# CustomerID não interfere na taxa de cancelamento, logo não será necessário manter esse dado
tabela = tabela.drop(columns='CustomerID')

# excluir da tabela os valores vazios, já que são poucos valores
tabela = tabela.dropna()

# verificar se existe dados vazios
print(tabela.info())

# Passo 4: Analisar os dados depois de limpos e começar o raciocinio 
print(tabela['cancelou'].value_counts()) # visualizar quantos cancelaram

print(tabela['cancelou'].value_counts(normalize=True).map("{:.1%}".format)) # visualizar quantos cancelaram em porcentagem

# Passo 5: Montar os gráficos para vê o que impacta no cancelamento. 
import plotly.express as px

# montar os gráficos em dois passos: criar o gráfico e exibir o gráfico
# criar o gráfico
grafico = px.histogram(tabela, x='duracao_contrato', color='cancelou')
# montar o gráfico
grafico.show()

# criar os graficos relacionando com todos os dados
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='cancelou', text_auto=True)

    grafico.show()

# Levantar os pontos chaves da observação:
    # P1: Pessoas com plano mensal cancelam 

    # P2: dias_atraso maior que 20 gera cancelamento

    # P3: ligacoes_callcenter mais de 4x gera cancelamento

# visualizar como ficaria a taxa de cancelamento se esses problemas fossem resolvidos

# resolvendo o P1:
tabela = tabela[tabela['duracao_contrato'] != 'Monthly'] # taxa caiu para 46%

# resolvendo P2:
tabela = tabela[tabela['dias_atraso'] <= 20] # taxa caiu para 35%

# resolvendo P3:
tabela = tabela[tabela['ligacoes_callcenter'] <= 4] # taxa caiu para 18%


print(tabela['cancelou'].value_counts(normalize=True).map("{:.1%}".format))
