import dash
from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from apps import navigation
import os

dash.register_page(__name__, path='/freelance',
                   title="Freelance", description="Here you can see temporary work I'm willing to do")

layout = html.Div(children=[
    navigation.navbar
])