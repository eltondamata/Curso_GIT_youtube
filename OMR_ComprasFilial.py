#eltondamata@gmail.com
# coding: utf-8


import pandas as pd

df = pd.read_pickle('~/Downloads/OMR_COMPRASFILIAL.pkl')
display(df)

df2 = df.groupby('DESTIPCNLVNDOMR')[['VLRVNDFATLIQ']].sum()
display(df2)
display(df2)s