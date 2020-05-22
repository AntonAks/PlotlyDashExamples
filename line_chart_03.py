import os
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

data_folder = os.path.join(os.path.dirname(__file__), 'data_samples/Data')
data_file = os.path.join(data_folder, '2010YumaAZ.csv')
df = pd.read_csv(data_file)

days = df['DAY'].unique() 

data = []

for day in days:
    trace = go.Scatter(x=df[df['DAY']==day].LST_TIME,
                        y=df[df['DAY']==day].T_HR_AVG,
                        mode='lines',
                        name=day)
    data.append(trace)


layout = go.Layout(title='Line Charts')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
