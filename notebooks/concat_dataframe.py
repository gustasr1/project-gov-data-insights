#%%

import pandas as pd
import glob

arquivos_csv = glob.glob('..\\data\\raw\\*.csv')

ls_dataframes = []

for arquivo in arquivos_csv:
    df_mes = pd.read_csv(arquivo, sep=";", encoding='latin-1')

    ls_dataframes.append(df_mes)

    df = pd.concat(ls_dataframes, ignore_index=True)

df.shape
# %%
#Teste de verificação quantidade de linhas em cada BD
df_teste = pd.read_csv('..\\data\\raw\\202506_CPGF.csv', sep=";", encoding="latin-1")
df_teste.shape
# %%

caminho = ('..\\data\\processed\\CPGF_consolidado.csv')

df.to_csv(caminho, sep=";", encoding='utf-8', index=False)
