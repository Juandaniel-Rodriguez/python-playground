# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
colors = {"background": "#000000", "text": "#6402c7"}
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


achievements = [{'name': 'promotion', 'date': '2022-02-24'},
                {'name': 'highschool graduation', 'date': '2021-02-25'}]

achievement_df = pd.DataFrame(achievements)

achievement_df['y_axis'] = 1

achievement_fig = px.scatter(achievement_df, x="date", y="y_axis", text="name",
                             title="Achievements in chronological order")

achievement_fig.update_traces(textposition="top center", marker={"symbol": 'star', 'size': 50, "color": "purple"})

achievement_fig.update_yaxes(visible=False)

skills = [
    {'name': 'Python', 'months': 2},
    {'name': 'Data viz', 'months': 1},
    {'name': 'Git', 'months': 2}
]

skills_df = pd.DataFrame(skills)

skills_df.sort_values(by='months', ascending=True, inplace=True)

skills_fig = px.bar(skills_df, x="months", y="name", orientation='h',
                    title="Skills")

achievement_fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])

skills_fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])

app_components = [
    html.H1(children='Juandaniel Portfolio',
            style={'color': colors['text'],
                   'backgroundColor': colors['background'],
                   'textAlign': 'center',

                   }),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=achievement_fig
    ),
    dcc.Graph(id='skills-fig-id', figure=skills_fig)
]

app.layout = html.Div(children=app_components, style={'backgroundColor': colors['background']})

if __name__ == '__main__':
    app.run_server(debug=True)
