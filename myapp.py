from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder()

app = Dash(__name__)
#for Render
server = app.server 

# Layout
app.layout = html.Div([
    html.H1("GDP Per Capita Over Time"),
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in df["country"].unique()],
        value="Canada"  # Default selection
    ),
    dcc.Graph(id="gdp-graph")
])

@app.callback(
    Output("gdp-graph", "figure"),
    Input("country-dropdown", "value")
)
def update_graph(selected_country):
    filtered_df = df[df["country"] == selected_country]
    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP Per Capita Over Time: {selected_country}",
        labels={"gdpPercap": "GDP Per Capita", "year": "Year"}
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)
