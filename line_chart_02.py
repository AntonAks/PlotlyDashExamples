import os
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

data_folder = os.path.join(os.path.dirname(__file__), 'data_samples/SourceData')
data_file = os.path.join(data_folder, 'nst-est2017-alldata.csv')
df = pd.read_csv(data_file)


df2 = df[df['DIVISION'] == '1']

df2.set_index('NAME', inplace=True)


list_of_papulation_columns = [col for col in df2.columns if col.startswith('POP')]

df2 = df2[list_of_papulation_columns]

data = [go.Scatter(x=df2.columns, 
                    y=df2.loc[name],
                    mode='lines',
                    name=name) for name in df2.index]


pyo.plot(data)