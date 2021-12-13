"""The Hidden Correlation Between Covid-19 and Hate Crimes in the United States
    From Jessica, Milena and Dian

Module Description
==================
This module contains the functions to show the total percent change from predicted to actual, in hate crime rate.
"""
from hate_crime import HateCrime
from covid_dataclass import CovidData

import plotly.graph_objects as go
import pandas as pd


def make_map() -> None:
    """Make sample map"""
    df = pd.read_csv('percent_diff.csv')

    for col in df.columns:
        df[col] = df[col].astype(str)

    df['text'] = df['State'] + '<br>' + \
        'Actual ' + df['Actual'] + '<br>' + \
        'Predicted ' + df['Predicted']

    fig = go.Figure(data=go.Choropleth(
        locations=df['State'],
        z=df['Percent Difference'].astype(float),
        locationmode='USA-states',
        colorscale='agsunset_r',
        autocolorscale=True,
        text=df['text'],  # hover text
        marker_line_color='white',
        colorbar_title="Percent Change"
    ))

    fig.update_layout(
        title_text='Hate Crime Rate to Covid Rate by State<br>(Hover for breakdown)',
        geo=dict(
            scope='usa',
            projection=go.layout.geo.Projection(type='albers usa'),
            showlakes=True,
            lakecolor='rgb(255, 255, 255)'),
    )

    fig.show()