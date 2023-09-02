import dash
from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from apps import navigation
import os

dash.register_page(__name__, path='/resume',
                   title="Resume", description="Here you can find my resume")

download_button = dbc.Container([
    dbc.Col(children=[
        dbc.Row(children=[
            html.Button("Click here to download", id='btn-download-resume'),
            dcc.Download(id="download-resume")
        ])
    ])

])

layout = html.Div(children=[
    navigation.navbar,
    download_button
])

# Callbacks
@callback(
    Output("download-resume", "data"),
    [Input("btn-download-resume", "n_clicks")],
    prevent_initial_callback=True
)
def download_resume(n_clicks):
    return dcc.send_file("\\assets\\resume\\"+os.listdir("\\assets\\resume\\"))


