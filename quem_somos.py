import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from navbar import Navbar
import base64
from dash.dependencies import Output, Input, State
nav = Navbar()
mauricio = base64.b64encode(open('Apoio/participantes/mauricio.jpeg', 'rb').read())
helon = base64.b64encode(open('Apoio/participantes/helon.jpeg', 'rb').read())
rafael_m = base64.b64encode(open('Apoio/participantes/rafael_m.jpeg', 'rb').read())
ademar = base64.b64encode(open('Apoio/participantes/ademar.jpeg', 'rb').read())
gabriel = base64.b64encode(open('Apoio/participantes/gabriel.jpeg', 'rb').read())
manu = base64.b64encode(open('Apoio/participantes/manu.jpeg', 'rb').read())
rafael = base64.b64encode(open('Apoio/participantes/rafael.jpeg', 'rb').read())
joao = base64.b64encode(open('Apoio/participantes/joao.jpeg', 'rb').read())

body_1 = dbc.CardGroup(
    [
dbc.Card(
    [

    dbc.CardImg(src='data:image/png;base64,{}'.format(mauricio.decode()), top=True,style={'height':'300px','object-fit': 'cover','object-position':'50% 50%'}),
    dbc.CardBody(
        [
            html.H4("Coordenador", className="card-title"),
            html.P(
                "Jose Mauricio Ramos de Souza Neto",
                className="card-text",
            ),
            dbc.Button("Lattes", color="primary",href='http://lattes.cnpq.br/6354668326581094'),
        ]
    ),



    ],
    style={"width": "18rem"},
),



dbc.Card([


    dbc.CardImg(src='data:image/png;base64,{}'.format(helon.decode()), top=True,style={'height':'300px','object-fit': 'cover','object-position':'50% 50%'}),
    dbc.CardBody(
        [
            html.H4("Coordenador Adjunto", className="card-title"),
            html.P(
                "Helon David de Macedo Braz",
                className="card-text",
            ),
            dbc.Button('Lattes', color="primary",href='http://lattes.cnpq.br/4756997631027455'),
        ]
    ),

    



    ],
    style={"width": "18rem"},
),



dbc.Card(
    [


    dbc.CardImg(src='data:image/png;base64,{}'.format(gabriel.decode()), top=True,style={'height':'300px','object-fit': 'cover','object-position':'50% 50%'}),
    dbc.CardBody(
        [
            html.H4("Bolsista Probex", className="card-title"),       
            html.P(
                "Gabriel Araujo Soares",
                className="card-text",
            ),
            dbc.Button("Lattes", color="primary",href='https://www.linkedin.com/in/gabriel-araujo-9709411a1/'),
        ]
    ),


     ],
    style={"width": "18rem"},
),


dbc.Card(
    [



    dbc.CardImg(src='data:image/png;base64,{}'.format(rafael.decode()), top=True,style={'height':'300px','object-fit': 'cover','object-position':'50% 50%'}),
    dbc.CardBody(
        [
            html.H4("Bolsista Probex", className="card-title"),
            html.P(
                "Rafael Pereira do Nascimento",
                className="card-text",
            ),
            dbc.Button("Lattes", color="primary",href='http://lattes.cnpq.br/8185636692888082'),
        ]
    ),



     ],
    style={"width": "18rem"},
),




   ],className="mb-4"
) 



body_2 = dbc.CardDeck(
    [

   
dbc.Card(
    [




    
    dbc.CardImg(src='data:image/png;base64,{}'.format(rafael_m.decode()), top=True,style={'height':'300px','object-fit': 'cover','object-position':'50% 50%'}),
    dbc.CardBody(
        [
            html.H4("Colaborador", className="card-title"),
            html.P(
                "Rafael de Sousa Marinho",
                className="card-text",
            ),
            dbc.Button("Lattes", color="primary",href='http://lattes.cnpq.br/9229841711516369'),
        ]
    ),

     ],
    style={"width": "18rem"},
),


      
dbc.Card(
    [

 



    dbc.CardImg(src='data:image/png;base64,{}'.format(ademar.decode()), top=True,style={'height':'300px','object-fit': 'cover','object-position':'50% 50%'}),
    dbc.CardBody(
        [
            html.H4("Colaborador", className="card-title"),
            html.P(
                "Ademar Virgolino da Silva Netto",
                className="card-text",
            ),
            dbc.Button("Lattes", color="primary",href='http://lattes.cnpq.br/5726596757497539'),
        ]
    ),


     ],
    style={"width": "18rem"},
),



      
dbc.Card(
    [

 

 
    dbc.CardImg(src='data:image/png;base64,{}'.format(manu.decode()), top=True,style={'height':'300px','object-fit': 'cover','object-position':'50% 50%'}),  
    dbc.CardBody(
        [
            html.H4("Voluntário", className="card-title"),
            html.P(
                "Emmanuela Tertuliano Moreira de Sousa",
                className="card-text",
            ),
            dbc.Button("Lattes", color="primary",href='http://lattes.cnpq.br/3424163405475839'),
        ]
    ),



     ],
    style={"width": "18rem"},
),


      
dbc.Card(
    [



    dbc.CardImg(src='data:image/png;base64,{}'.format(joao.decode()), top=True,style={'height':'300px','object-fit': 'cover','object-position':'50% 50%'}),
    dbc.CardBody(
        [
            html.H4("Voluntário", className="card-title"),
            html.P(
                "João Guilherme Sales de Oliveira",
                className="card-text",
            ),
            dbc.Button("Lattes", color="primary",href='http://lattes.cnpq.br/9540990930501608'),
        ]
    ),


     ],
    style={"width": "18rem"},
),






       ])

def quem_somos():
    layout = html.Div([
    nav,
    html.Div(html.Br()),
    html.H1('Equipe', className="display-3",style={ 'textAlign':'center','color':'#04383f'}),
    html.Div(html.Br()),
    body_1,
    body_2
    ])
    return layout



 
