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
                    x=df[df['timeframe'] == i]['R1'],
                    y=df[df['timeframe'] == i]['G1'],
                    text=df[df['timeframe'] == i]['media'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'},
			'color': df[df['timeframe'] == i]['R1']  
                    },
                    name=i
                ) for i in df['timeframe'].unique()
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
