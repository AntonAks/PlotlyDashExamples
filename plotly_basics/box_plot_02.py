import os
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data_samples/Data')
data_file = os.path.join(data_folder, 'abalone.csv')
df = pd.read_csv(data_file)


data = [go.Box(y=df[df['sex']=='M']['diameter'], name='M', boxpoints='all', jitter=0.3),
        go.Box(y=df[df['sex']=='F']['diameter'], name='F', boxpoints='all', jitter=0.3),]

pyo.plot(data)




