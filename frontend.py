import os
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from backend import calcular_resultados

# Obtén la ruta del directorio actual
current_directory = os.getcwd()

# Ruta del directorio de activos
assets_folder = os.path.join(current_directory, 'assets')

# Configura el directorio de activos en la aplicación Dash
app = dash.Dash(__name__, assets_folder=assets_folder, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1('Calculadora de Suelos'),
    html.Div([
        html.Label('Peso húmedo del suelo (en Kg)'),
        dcc.Input(id='peso-total', type='number', placeholder='Ingrese el peso húmedo del suelo')
    ]),
    html.Div([
        html.Label('Peso seco del suelo (en Kg)'),
        dcc.Input(id='peso-solidos', type='number', placeholder='Ingrese el peso seco del suelo')
    ]),
    html.Div([
        html.Label('Gravedad específica'),
        dcc.Input(id='gravedad-especifica', type='number', placeholder='Ingrese la gravedad específica')
    ]),
    html.Div([
        html.Label('Volumen total del suelo (en m³)'),
        dcc.Input(id='volumen-total', type='number', placeholder='Ingrese el volumen total del suelo')
    ]),
    html.Button('Calcular', id='calcular-button', className='btn btn-primary mt-3'),
    html.Div(id='resultados-div'),

    dbc.Container([
        html.Img(src="/assets/img/diagrama.jpg", style={'width': '50%'})
    ], className="text-center mt-4")
])

@app.callback(
    Output('resultados-div', 'children'),
    [Input('calcular-button', 'n_clicks')],
    [State('peso-total', 'value'),
     State('peso-solidos', 'value'),
     State('gravedad-especifica', 'value'),
     State('volumen-total', 'value')]
)
def actualizar_resultados(n_clicks, peso_total, peso_solidos, gravedad_especifica, volumen_total):
    if n_clicks and n_clicks > 0:
        # Validar los valores ingresados antes de llamar a la función calcular_resultados
        if peso_total is not None and peso_solidos is not None and gravedad_especifica is not None and volumen_total is not None:
            resultados = calcular_resultados(peso_total, peso_solidos, gravedad_especifica, volumen_total)
            if resultados:
                # Extraer los valores relevantes de los resultados
                volumen_vacios = resultados['volumen_vacios']
                volumen_aire = resultados['volumen_aire']
                volumen_agua = resultados['volumen_agua']
                volumen_particulas_solidas = resultados['volumen_particulas_solidas']
                volumen_total = resultados['volumen_total']
                peso_total = resultados['peso_humedo']
                peso_agua = resultados['peso_agua']
                peso_seco = resultados['peso_seco']
                humedad = resultados['humedad']
                relacion_vacios = resultados['relacion_vacios']
                porosidad = resultados['porosidad']
                peso_unitario_humedo = resultados['peso_unitario_humedo']
                peso_unitario_particulas_solidas = resultados['peso_unitario_particulas_solidas']
                peso_unitario_seco = resultados['peso_unitario_seco']
                gravedad_especifica = resultados['gravedad_especifica']
                saturacion_relativa = resultados['saturacion_relativa']

                # Mostrar los resultados en el resultados-div
                return [
                    html.P(f'Volumen vacíos: {volumen_vacios:.2f}m³'),
                    html.P(f'Volumen aire: {volumen_aire:.2f}m³'),
                    html.P(f'Volumen agua: {volumen_agua:.2f}m³'),
                    html.P(f'Volumen solidos: {volumen_particulas_solidas:.2f}m³'),
                    html.P(f'Volumen total: {volumen_total:.2f}m³'),
                    html.P(f'Peso húmedo: {peso_total:.2f}Kg'),
                    html.P(f'Peso del agua: {peso_agua:.2f}Kg'),
                    html.P(f'Peso seco: {peso_seco:.2f}Kg'),
                    html.P(f'Humedad: {humedad:.2f}%'),
                    html.P(f'Relación de vacios: {relacion_vacios:.2f}'),
                    html.P(f'Porosidad: {porosidad:.2f}'),
                    html.P(f'Peso unitario húmedo: {peso_unitario_humedo:.2f}Kg/m³'),
                    html.P(f'Peso unitario de las particulas solidas: {peso_unitario_particulas_solidas:.2f}Kg/m³'),
                    html.P(f'Peso unitario seco: {peso_unitario_seco:.2f}Kg/m³'),
                    html.P(f'Gravedad especifica: {gravedad_especifica:.2f}'),
                    html.P(f'Saturación relativa: {saturacion_relativa:.2f}%'),
                ]
            else:
                return html.P('Error: Verifique los valores ingresados.')

        else:
            return html.P('Error: Verifique los valores ingresados.')

    else:
        return None