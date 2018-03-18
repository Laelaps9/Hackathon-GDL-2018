import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
print ("Hola")
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_columns', 27)

df = pd.ExcelFile('../Data/2007.xlsx').parse('BDRAM_2007')
#df = pd.ExcelFile('../Data/2008.xlsx').parse('BDRAM_2008')
#df = pd.ExcelFile('../Data/2009.xlsx').parse('BDRAM_09')
#df = pd.ExcelFile('../Data/2010.xlsx').parse('BDRAM_2010')
#df = pd.ExcelFile('../Data/2011.xlsx').parse('Data')

df_CO = (df['PARAMETRO'] == 'CO')
df_NO2 = (df['PARAMETRO'] == 'NO2')
df_NOX = (df['PARAMETRO'] == 'NOX')
df_O3 = (df['PARAMETRO'] == 'O3')
df_PM10 = (df['PARAMETRO'] == 'PM10')
df_SO2 = (df['PARAMETRO'] == 'SO2')
df_AGU = (df['CLAVE_EST'] == 'AGU')
df_CEN = (df['CLAVE_EST'] == 'CEN')
df_LDO = (df['CLAVE_EST'] == 'LDO')
df_MIR = (df['CLAVE_EST'] == 'MIR')
df_OBL = (df['CLAVE_EST'] == 'OBL')
df_TLA = (df['CLAVE_EST'] == 'TLA')
df_VAL = (df['CLAVE_EST'] == 'VAL')
df_H1 =  (df['HORA01'])
df_H2 =  (df['HORA02'])
df_H3 =  (df['HORA03'])
df_H4 =  (df['HORA04'])
df_H5 =  (df['HORA05'])
df_H6 =  (df['HORA06'])
df_H7 =  (df['HORA07'])
df_H8 =  (df['HORA08'])
df_H9 =  (df['HORA09'])
df_H10 = (df['HORA10'])
df_H11 = (df['HORA11'])
df_H12 = (df['HORA12'])
df_H13 = (df['HORA13'])
df_H14 = (df['HORA14'])
df_H15 = (df['HORA15'])
df_H16 = (df['HORA16'])
df_H17 = (df['HORA17'])
df_H18 = (df['HORA18'])
df_H19 = (df['HORA19'])
df_H20 = (df['HORA20'])
df_H21 = (df['HORA21'])
df_H22 = (df['HORA22'])
df_H23 = (df['HORA23'])
df_H24 = (df['HORA24'])

count = 0
j = 0
k = 0
def promedioDias(dfa, dfp):
    dias = []
    df_TEMP = (dfa & dfp)
    for i in range(len(df)):
        if(pd.Series(df_TEMP).iloc[i]) == 1:
            sumaHoras = 0
            sumaHoras += float(pd.Series(df_H1).iloc[i])
            sumaHoras += float(pd.Series(df_H2).iloc[i])
            sumaHoras += float(pd.Series(df_H3).iloc[i])
            sumaHoras += float(pd.Series(df_H4).iloc[i])
            sumaHoras += float(pd.Series(df_H5).iloc[i])
            sumaHoras += float(pd.Series(df_H6).iloc[i])
            sumaHoras += float(pd.Series(df_H7).iloc[i])
            sumaHoras += float(pd.Series(df_H8).iloc[i])
            sumaHoras += float(pd.Series(df_H9).iloc[i])
            sumaHoras += float(pd.Series(df_H10).iloc[i])
            sumaHoras += float(pd.Series(df_H11).iloc[i])
            sumaHoras += float(pd.Series(df_H12).iloc[i])
            sumaHoras += float(pd.Series(df_H13).iloc[i])
            sumaHoras += float(pd.Series(df_H14).iloc[i])
            sumaHoras += float(pd.Series(df_H15).iloc[i])
            sumaHoras += float(pd.Series(df_H16).iloc[i])
            sumaHoras += float(pd.Series(df_H17).iloc[i])
            sumaHoras += float(pd.Series(df_H18).iloc[i])
            sumaHoras += float(pd.Series(df_H19).iloc[i])
            sumaHoras += float(pd.Series(df_H20).iloc[i])
            sumaHoras += float(pd.Series(df_H21).iloc[i])
            sumaHoras += float(pd.Series(df_H22).iloc[i])
            sumaHoras += float(pd.Series(df_H23).iloc[i])
            sumaHoras += float(pd.Series(df_H24).iloc[i])
            dias.append(sumaHoras/24)
    dias.append(-1)
    return dias

#promedioDias(df_AGU, df_CO)
counter = 0
anual = 0
a = promedioDias(df_AGU, df_O3)
while(a[counter] != -1):
    print(a[counter])
    anual += a[counter]
    counter += 1
#print(anual / (counter-1))
