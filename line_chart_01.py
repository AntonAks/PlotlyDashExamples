import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

random_x = np.linspace(0, 1, 100)
random_y = np.random.randn(100)


trace0 = go.Scatter(x=random_x, 
                    y=random_y + 5, 
                    mode="markers",
                    name="markers"
                    )

trace1 = go.Scatter(x=random_x, 
                    y=random_y, 
                    mode="lines",
                    name="lines"
                    )


trace2 = go.Scatter(x=random_x, 
                    y=random_y - 5, 
                    mode="lines+markers",
                    name="lines+markers"
                    )


data = [trace0, trace1, trace2]


layout = go.Layout(title='Line Charts')


fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='line_chart.html')
