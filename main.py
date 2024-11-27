import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from data import countries_df, totals_df, dropdown_options, make_global_df, make_country_df
from builders import make_table
from dash.dependencies import Input, Output

# Dash 애플리케이션 초기화 (external_stylesheets는 필요 없음, assets 폴더가 자동으로 로딩됨)
app = dash.Dash(__name__)



# 예시 데이터 생성 (countries_df, totals_df는 이미 정의된 데이터프레임으로 가정)
bubble_map = px.scatter_geo(
    countries_df,
    size="Confirmed",
    title="Confirmed By Country",
    hover_name="Country_Region",
    color="Confirmed",
    locations="Country_Region",
    locationmode="country names",
    size_max=40,
    template="plotly_dark",
    color_continuous_scale=px.colors.sequential.Oryel,
    hover_data={
        "Confirmed": ":,.2f",
        "Deaths": ":,.2f",
        "Recovered": ":,.2f",
        "Country_Region": False,
    },
)

bubble_map.update_layout(margin=dict(l=0, r=0, t=50, b=0))

bars_graph = px.bar(
    totals_df,
    x="condition",
    hover_data={"count": ":,"},
    y="count",
    template="plotly_dark",
    title="Total Global Cases",
    labels={"condition": "Condition", "count": "Count", "color": "Condition"},
)

bars_graph.update_traces(marker_color=["#e74c3c", "#8e44ad", "#27ae60"])

# 레이아웃 설정
app.layout = html.Div(
    children=[
        html.Header(
            children=[html.H1("Corona Dashboard")],
            className="header"
        ),
        html.Div(
            className="grid-container",
            children=[
                html.Div(
                    className="graph-container",
                    children=[dcc.Graph(figure=bubble_map)],
                ),
                html.Div(children=[make_table(countries_df)])
            ]
        ),
        html.Div(
            className="grid-container",
            children=[
                html.Div(
                    children=[dcc.Graph(figure=bars_graph)]
                ),
                html.Div(
                     className="graph-container",
                    children=[
                        dcc.Dropdown(
                            placeholder="Select a Country",
                            id="country",
                            options=[
                                {"label": country, "value": country}
                                for country in dropdown_options
                            ],
                        ),
                        dcc.Graph(id="country_graph"),
                    ]
                ),
            ],
        ),
    ]
)

@app.callback(Output("country_graph", "figure"), [Input("country", "value")])
def update_hello(value):
    if value:
        df = make_country_df(value)
    else:
        df = make_global_df()
    fig = px.line(
        df,
        x="date",
        y=["confirmed", "deaths", "recovered"],
        template="plotly_dark",
        labels={"value": "Cases", "variable": "Condition", "date": "Date"},
        hover_data={"value": ":,", "variable": False, "date": False},
    )
    fig.update_xaxes(rangeslider_visible=True)
    fig["data"][0]["line"]["color"] = "#e74c3c"
    fig["data"][1]["line"]["color"] = "#8e44ad"
    fig["data"][2]["line"]["color"] = "#27ae60"
    return fig
    

if __name__ == '__main__':
    app.run_server(debug=True)
