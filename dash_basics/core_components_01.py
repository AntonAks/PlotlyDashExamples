import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[{'label': 'Anton',
                           'value': 'Developer'},
                          {'label': 'Nick',
                           'value': 'QA'},
                          {'label': 'Alice',
                           'value': 'CEO'}],
                 value='CEO'),
    html.Label('Slider'),
    dcc.Slider(min=-10, max=10, step=1, value=0,
               marks={i: i for i in range(-10, 10)}),
    html.Label('Ration Items'),
    dcc.RadioItems(options=[{'label': 'Anton',
                             'value': 'Developer'},
                            {'label': 'Nick',
                             'value': 'QA'},
                            {'label': 'Alice',
                             'value': 'CEO'}],
                   value='QA')

])


if __name__ == '__main__':
    app.run_server()
