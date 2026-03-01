import dash
from dash import Dash, html, dcc, dash_table, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_excel('./CamFruitWebsite.xlsx', sheet_name='Sheet1')

app = Dash(__name__)

app.title = "🫐🍎🥝🍓🍋🥭🍍🍊🍈🍐🍉🍒🍌"

app.layout = html.Div([
    html.H1("Cam's Fruit Rankings 🫐🍎🥝🍓🍋🥭🍍🍊🍈🍐🍉🍒🍌"),
    html.P([
        "Created by Kate, to be further developed by ",
        html.Span("Hacker Cam (TM)", style={"color": "blue", "fontWeight": "bold"})
    ]),
    dash_table.DataTable(
        id="table",
        data=df.to_dict("records"),
        columns=[{"name": i, "id": i} for i in df.columns],

        filter_action="native",
        sort_action="native",
        row_selectable="multi",
        page_size=10
    ),

    dcc.Graph(id="plot")

])

@app.callback(
    Output("plot", "figure"),
    Input("table", "derived_virtual_data"),
    Input("table", "derived_virtual_selected_rows"),
)
def update_graph(rows, selected_rows):

    dff = pd.DataFrame(rows)
    if "Rating" in dff.columns:
        dff = dff.sort_values(by="Rating", ascending=False)

    if selected_rows:
        dff = dff.iloc[selected_rows]
    
    if "Fruit" in dff.columns:

        fig = px.bar(dff, x="Fruit", y="Rating", title="Cam's Fruit Rankings", color="Fruit")


        return fig


if __name__ == "__main__":
    app.run(debug=True)