import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

markdown_text = '''
### Dash and Markdown example
Link example [Commonmark](https://commonmark.org/)
Some **bold** text
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server()
