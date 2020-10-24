from sqlalchemy import create_engine
import pandas as pd 

engine = create_engine(
        "mysql+mysqlconnector://root:rootdb@localhost/enem",
                isolation_level="READ UNCOMMITTED"
            )

csvname = 'MICRODADOS_ENEM_2019_FILTRADO.csv'
#df = pd.read_csv(csvname, sep=";", encoding="ISO-8859-1")

for df_chunk in pd.read_csv(csvname,sep=";", 
               low_memory=False,encoding= "ISO-8859-1",chunksize=1000):
    #temp_df = chunk.loc[chunk['SG_UF_PROVA'] == 'RS']
    #break
    df_chunk["ano"] = "2019"
    df_chunk.to_sql("microdados", con = engine, if_exists = "append")

#print (df.head())
