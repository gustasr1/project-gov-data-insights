# %%

import pandas as pd

df = pd.read_csv('..\\data\\processed\\CPGF_consolidado.csv', sep=';')
df.head()

# %%
#Renomeando e padronizando colunas
df.rename(columns={"CÓDIGO ÓRGÃO SUPERIOR": "cod_orgao_superior", 'NOME ÓRGÃO SUPERIOR': 'nome_orgao_superior',	\
                   'CÓDIGO ÓRGÃO': 'cod_orgao',	'NOME ÓRGÃO': 'nome_orgao',	'CÓDIGO UNIDADE GESTORA': 'cod_unid_gestora',	'NOME UNIDADE GESTORA': 'nome_unid_gestora',	\
                    'ANO EXTRATO': 'ano_extrato', 'MÊS EXTRATO': 'mes_extrato',	'CPF PORTADOR':'cpf_portador',	'NOME PORTADOR':'nome_portador', 'CNPJ OU CPF FAVORECIDO': 'cnpj_cpf_favorecido', \
                            	'NOME FAVORECIDO':'nome_favorecido',	'TRANSAÇÃO': 'transacao',	'DATA TRANSAÇÃO':'data_transacao',	'VALOR TRANSAÇÃO':'valor_transacao'}, inplace=True)

# %%
#Tratamento de valores nulos
df.isnull().sum()
df['cpf_portador']= df['cpf_portador'].fillna('sigiloso')

# %%
#Removendo duplicatas - Não será removido pois não há dados de identificador ú
# nico
df.duplicated().sum()
df[df.duplicated(keep=False)]

# %%

#Ajustando Dtypes
df.dtypes
#%%
df = df.astype({
	'cod_orgao_superior' : 'category',
    'nome_orgao_superior' : 'category',
	'cod_orgao' : 'category',
	'nome_orgao' : 'category',
	'cod_unid_gestora' : 'category',
	'nome_unid_gestora' : 'category'
})
# %%

df['data_transacao'] = pd.to_datetime(df['data_transacao'])
# %%

#Replace para transformar coluna em float
df['valor_transacao'] = df['valor_transacao'].str.replace(',','.').astype(float)

# %%
df['cpf_portador'] = df['cpf_portador'].astype(str)
# %%
df['cnpj_cpf_favorecido'] = df['cnpj_cpf_favorecido'].astype(str)
# %%

colunas_categ = [
    'nome_orgao_superior', 
    'nome_orgao', 
    'nome_unid_gestora', 
    'nome_portador', 
    'nome_favorecido', 
    'transacao'
]

for coluna in colunas_categ:
	df[coluna] = df[coluna].str.strip().str.title().astype('category')

# %%
df.to_csv('..\\data\\processed\\CPGF_consolidado_final.csv', sep=';', encoding='utf-8-sig')
