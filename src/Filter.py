import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_columns', 10)

df = pd.ExcelFile('../Data/1996.xlsx').parse('BDRAM_1996')
df_filtered = (df['CLAVE_EST'] == 'AGU')
print(df[df_filtered])
