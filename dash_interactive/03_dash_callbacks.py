import os
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

import plotly.graph_objects as go
import pandas as pd

data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data_samples/Data')
data_file = os.path.join(data_folder, 'mpg.csv')
df = pd.read_csv(data_file)

features = df.columns

app = dash.Dash()

app.layout = html.Div([

    html.Div([
        dcc.Dropdown(
            id='xaxis',
            options=[{'label': i.title(), 'value': i} for i in features],
            value='displacement'
        )
    ],
        style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='yaxis',
            options=[{'label': i.title(), 'value': i} for i in features],
            value='acceleration'
        )
    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

    dcc.Graph(id='feature-graphic')
], style={'padding': 10})


@app.callback(
    Output('feature-graphic', 'figure'),
    [Input('xaxis', 'value'),
     Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):
    return {
        'data': [go.Scatter(
            x=df[xaxis_name],
            y=df[yaxis_name],
            text=df['name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={'title': xaxis_name.title()},
            yaxis={'title': yaxis_name.title()},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server()
