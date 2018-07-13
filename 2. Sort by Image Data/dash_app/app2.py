import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

import numpy as np

app = dash.Dash()

df = pd.read_csv( '../colors.csv', sep=';')

import csv
ColCat = []
with open('../colors.csv', 'rt') as csvfile:
    myreader = csv.reader(csvfile, delimiter=';')
    for row in myreader:
        ColCat.append(row)

app.layout = html.Div([
    dcc.Graph(
        id='WebGal',
        figure={
            'data': [
                go.Scatter(
                    x=ColCat[i][0],
                    y=ColCat[i][1],
                    text=ColCat[i][7],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'},
			'color': 'black'
                    },
                    name=i
                ) for i in range(len(ColCat))
            ],
            'layout': go.Layout(
                xaxis={'title': 'Redness'},
                yaxis={'title': 'Greenness'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()
