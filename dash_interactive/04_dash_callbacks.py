import os
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

import plotly.graph_objects as go
import pandas as pd
import base64


data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data_samples/Data')
data_file = os.path.join(data_folder, 'wheels.csv')
df = pd.read_csv(data_file)

app = dash.Dash()


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return f'data:image/png;base64,{encoded.decode()}'


app.layout = html.Div([
    dcc.RadioItems(
        id='wheels',
        options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
        value=1
    ),
    html.Div(id='wheels-output'),

    html.Hr(),  # add a horizontal rule
    dcc.RadioItems(
        id='colors',
        options=[{'label': i, 'value': i} for i in df['color'].unique()],
        value='blue'
    ),
    html.Div(id='colors-output'),
    html.Img(id='display-image', src='children', height=300)
], style={'fontFamily':'helvetica', 'fontSize':18})


@app.callback(Output('wheels-output', 'children'),
             [Input('wheels', 'value')])
def callback_a(wheels_values):
    return f"you chose {wheels_values}"


@app.callback(Output('colors-output', 'children'),
             [Input('colors', 'value')])
def callback_b(colors_values):
    return f"you chose {colors_values}"


@app.callback(Output('display-image', 'src'),
             [Input('wheels', 'value'),
              Input('colors', 'value')])
def callback_image(wheel, color):
    path = os.path.join(data_folder, 'Images')
    return encode_image(path + '\\' + df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])


if __name__ == '__main__':
    app.run_server()
