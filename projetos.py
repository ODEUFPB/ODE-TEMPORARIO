import dash
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
from dash.dependencies import Input, Output
import plotly.offline as py
from plotly.graph_objs import *   
import plotly.graph_objs as go 
import dash_bootstrap_components as dbc
import folium  
from folium import IFrame, FeatureGroup 
import numpy as np
from PIL import Image
import json
import os  
import base64 
import glob  
import pandas as pd 
from folium.plugins import MarkerCluster   



### Data
import pandas as pd
import pickle
### Graphing
import plotly.graph_objects as go
### Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
## Navbar
from navbar import Navbar

nav = Navbar()   

 


centros = ['Todos os Centros','CCS','CEAR','CCEN','CT','CCM','CBIOTEC','CTDR','CCHLA','CCTA','CCHSA','CCSA','CI','CCAE','CCJ','CCA','CE']
anos = ['Todos os Anos', 2017,2018,2019]


card_content = [
    dbc.CardHeader("Opções de filtro",style={'font-size':24, 'textAlign':'center'}),
    dbc.CardBody(
        [


    html.H4("Escolha o ano desejado:", style={'font-size':19}),
        dcc.Dropdown(
        id = 'anos_projetos',
        placeholder="Selecione o(s) ano(s)",
        options=[
            {'label': j, 'value': j} for j in anos  
        ],
        value=['2019'],   
        multi=True,
    searchable=False
    ),


    html.Div(html.Br()),

        html.H4("Escolha o centro desejado:", style={'font-size':19}),
        dcc.Dropdown(
        id = 'centros_projetos',
        placeholder="Selecione o(s) centro(s)",  
        options=[
            {'label': j, 'value': j} for j in centros  
        ],
        value=['CEAR'],   
        multi=True,
    searchable=False
    ),
    

html.Br(),
html.H4("Digite o título do projeto desejado:", style={'font-size':19}),
dcc.Input(
        id='entrada_titulo_projetos',
        placeholder='Escreva o título do projeto',
        type='text',
        value = '',
        style={'margin-bottom':'10px'}
),

   
html.Button('Pesquisar', id='btn-nclicks-1', n_clicks=0),

html.Div(html.Br()),
html.H4("Escolha um projeto para ver o resumo:", style={'font-size':19}),
        dbc.Select(
        id = 'projetos_projetos',  
        options=[
            {'label': j, 'value': j} for j in []  
        ],
        value=[''],   
        ),




        ]
    ),
]

jumbotron = dbc.Card(card_content,  outline=True)

card_content_3 = [
    dbc.CardHeader("Resumo do projeto",style={'font-size':24, 'textAlign':'center'}),
    dbc.CardBody(
        [
        dcc.Textarea(
        id='textarea_example',
        readOnly=True,
        value='',
        style={'display':'block', 'max-width': '100%', 'margin-left': 'auto', 'margin-right': 'auto','width':'90%','height':'580px','textAlign':'justify', 'font-size':20},
    ),
    #html.Div(id='textarea_example_output', style={'whiteSpace': 'pre-line'})
        ]
    ),
]

jumbotron_2 = dbc.Card(card_content_3,  outline=True)

body_1 =html.Div([  


        dbc.Row(
           [
               dbc.Col(
                  [

                jumbotron,



                   ], md=4

               ),
              dbc.Col([
              jumbotron_2 

                    ], md=8 ),

                ],no_gutters=True
            ),
              
])

modal_6 = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader("ERROR"),
                dbc.ModalBody("Escolha pelo menos um ano como parâmetro de entrada de anos"),
                dbc.ModalFooter(
                dbc.Button("Close", id="close_6", className="ml-auto")
                ),
            ],
            id="modal_6",
        ),
    ]
)

modal_7 = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader("ERROR"),
                dbc.ModalBody("Escolha pelo menos um centro como parâmetro de entrada de centros"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close_7", className="ml-auto")
                ),
            ],
            id="modal_7",
        ),
    ]
)




def projetos():
    layout = html.Div([
    nav,
    body_1,
    modal_6,
    modal_7
    ])
    return layout



