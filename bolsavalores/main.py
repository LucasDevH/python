import pandas as pd
import matplotlib.pyplot as plt

# Importar arquivo CSV
vale3_df = pd.read_csv('C:\\Users\\lucas\\Desktop\\python\\bolsavalores\\vale3.csv')

# Criar novo DataFrame com as colunas de DATA e FECHAMENTO
vale3_resumo = vale3_df[['DATA', 'FECHAMENTO']].copy()
vale3_resumo.columns = ['data', 'fechamento']

# Substituir as virgulas por ponto na coluna fechamento
vale3_resumo['fechamento'] = vale3_resumo['fechamento'].str.replace(',' , '.').astype(float)

# Exportar arquivo para novo arquivo CSV
vale3_resumo.to_csv('C:\\Users\\lucas\\Desktop\\python\\bolsavalores\\vale3_resumo.csv', index=False)

# Verificar preço medio dos papeis

preco_medio = vale3_resumo['fechamento'].mean()
print('O preço medio da Ação foi de R${:.2f} ' .format(preco_medio))

# Preço Maximo e Preço Minimo

preco_min = vale3_resumo['fechamento'].min()
data_max = vale3_resumo.loc[vale3_resumo['fechamento'].idxmax(), 'data']
preco_max = vale3_resumo['fechamento'].max()
data_min = vale3_resumo.loc[vale3_resumo['fechamento'].idxmin(), 'data']

print('O preço maximo da ação foi de R${:.2f} na data {}'.format(preco_max, data_max))
print('O preço minimo da ação foi de R${:.2f} na data {}'.format(preco_min, data_min))

# Valor das ações  no dia 70 e lucro ou prejuizo no momento

acoes_adquiridas = 2000
data_aquisiacao = vale3_resumo.iloc[9]['data']
preco_aquisicao = vale3_resumo.iloc[9]['fechamento']

data_venda = vale3_resumo.iloc[69]['data']
preco_venda = vale3_resumo.iloc[69]['fechamento']

valor_investido = acoes_adquiridas * preco_aquisicao
valor_venda = acoes_adquiridas * preco_venda

print('O valor total das ações no dia 10: R${:.2f}'.format(valor_investido))
print('O valor total das ações no dia 70: R${:.2f}'.format(valor_venda))

lucro_prejuizo = valor_venda - valor_investido

#print(f'O investidor teve {"lucro" if lucro_prejuizo > 0 else "prejuizo"} de R$ {lucro_prejuizo}')

if lucro_prejuizo > 0:
    print('Esta no LUCRO em R${:.2f}'.format(lucro_prejuizo))
else:
    print('Esta no PREJUIZO de R${:.2f}'.format(lucro_prejuizo))

# Converter a coluna Data para formato datetime

vale3_resumo['data'] = pd.to_datetime(vale3_resumo['data'], format="%d/%m/%Y")

# Criar Grafico

plt.figure(figsize=(12, 6))
plt.plot(vale3_resumo['data'], vale3_resumo['fechamento'], label='fechamento', color='blue')
plt.title('Preço de fechamento da VALE3')
plt.xlabel('data')
plt.ylabel('fechamento')
plt.legend()
plt.grid(True)
plt.show()