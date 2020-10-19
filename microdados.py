import pandas as pd

df = pd.read_csv("microdados_2019_100000.csv", engine='python', sep=';')
ext = df[['NU_INSCRICAO', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO' ]]
print (ext)

ext.to_csv("extracted.csv",sep=";")
