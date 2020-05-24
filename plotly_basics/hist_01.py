import os
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data_samples/Data')
data_file = os.path.join(data_folder, 'mpg.csv')
df = pd.read_csv(data_file)


data = [go.Histogram(x=df['mpg'],
                    xbins=dict(start=0, end=50, size=1))]

layout = go.Layout(title = 'Histogram')

fig = go.Figure(data, layout)
pyo.plot(fig)