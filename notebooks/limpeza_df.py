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
#ano extrato mes extrato e data transação
