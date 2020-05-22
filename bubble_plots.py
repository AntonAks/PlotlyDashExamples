import os
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


data_folder = os.path.join(os.path.dirname(__file__), 'data_samples/Data')
data_file = os.path.join(data_folder, 'mpg.csv')
df = pd.read_csv(data_file)

data = [go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'],
                    mode='markers', 
                    marker=dict(size=df['weight']/100, 
                                color=df['cylinders'],
                                showscale=True),
                    
                    )]

layout = go.Layout(title="Bubble Chart", hovermode='closest')

fig = go.Figure(data,layout)

pyo.plot(fig)