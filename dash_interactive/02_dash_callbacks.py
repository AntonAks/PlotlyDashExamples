import os
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

import plotly.graph_objects as go
import pandas as pd


data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data_samples/Data')
data_file = os.path.join(data_folder, 'gapminderDataFiveYear.csv')
df = pd.read_csv(data_file)

year_options = []

years_list = list(df['year'].unique())
years_list.sort(reverse=True)


for year in years_list:
    year_options.append({'label':str(year), 'value':year})


app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker',
                options=year_options)
])


@app.callback(Output('graph', 'figure'), 
            [Input('year-picker', 'value')])
def update_figure(selected_year):
    if not selected_year:
        selected_year = years_list[0]
    filtered_df = df[df['year']==selected_year]

    traces = []

    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']==continent_name]
        traces.append(go.Scatter(
            x = df_by_continent['gdpPercap'],
            y = df_by_continent['lifeExp'],
            mode = 'markers',
            opacity = 0.7,
            marker = {'size':15},
            name = continent_name
        ))
        
    return {'data': traces, 
            'layout': go.Layout(title=f'My Plot. {selected_year} Year', 
                                xaxis={'title': 'GDP Per Cap'},
                                yaxis={'title': 'Life Expectancy'})}

if __name__ == "__main__":
    app.run_server()

