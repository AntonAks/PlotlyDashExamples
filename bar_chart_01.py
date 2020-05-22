import os
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


data_folder = os.path.join(os.path.dirname(__file__), 'data_samples/Data')
data_file = os.path.join(data_folder, '2018WinterOlympics.csv')
df = pd.read_csv(data_file)


trace1 = go.Bar(x=df['NOC'], 
                y=df['Gold'],
                name='Gold',
                marker=dict(color='#FFD700'))

trace2 = go.Bar(x=df['NOC'], 
                y=df['Silver'],
                name='Silver',
                marker=dict(color='#9EA0A1'))

trace3 = go.Bar(x=df['NOC'], 
                y=df['Bronze'],
                name='Bronze',
                marker=dict(color='#CD7F32'))


# 1st Bar
# data = [go.Bar(x=df['NOC'], y=df['Total'])]


data = [trace1, trace2, trace3]

layout = go.Layout(title='Medals', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)


