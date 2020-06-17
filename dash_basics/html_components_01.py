import dash
import dash_html_components as html


app = dash.Dash()


app.layout = html.Div(['This is outermost Div',
                       html.Div('Inner div', style={'color': 'red'}),
                       html.Div('Another inner div', style={'color': 'blue',
                                                            'border': '1px blue solid',
                                                            'margin': 10})],
                      style={'color': 'green',
                             'border': '2px green solid'}
                      )


if __name__ == '__main__':
    app.run_server()
