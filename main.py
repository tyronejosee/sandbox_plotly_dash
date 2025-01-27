import io
import base64

import dash
from dash import dcc, Input, Output
from dash.html import Div, H1, Button
from pandas import DataFrame
from plotly.graph_objs._figure import Figure

from app.processor import process_excel
from app.figures import (
    create_bar_chart,
    create_line_chart,
    create_pie_chart,
    create_scatter_chart,
)

app = dash.Dash(__name__)

app.layout = Div(
    [
        H1("Dashboard"),
        dcc.Upload(
            id="upload-data",
            children=Button("Subir archivo..."),
            multiple=False,
        ),
        Div(id="output-data-upload"),
    ],
    style={
        "margin": "0 auto",
        "paddingLeft": "20px",
        "paddingRight": "20px",
    },
)


@app.callback(
    Output("output-data-upload", "children"),
    Input("upload-data", "contents"),
)
def actualizar_grafico(uploaded_file) -> Div:
    if uploaded_file is None:
        return Div(["Por favor, sube un archivo Excel."])

    _, content_string = uploaded_file.split(",")
    decoded = base64.b64decode(content_string)
    input_file = io.BytesIO(decoded)
    dataframe: DataFrame = process_excel(input_file)

    if dataframe.empty:
        return Div(["Error al procesar el archivo."])

    bar_chart: Figure = create_bar_chart(dataframe)
    line_chart: Figure = create_line_chart(dataframe)
    pie_chart: Figure = create_pie_chart(dataframe)
    scatter_chart: Figure = create_scatter_chart(dataframe)

    return Div(
        [
            dcc.Graph(figure=bar_chart),
            dcc.Graph(figure=line_chart),
            dcc.Graph(figure=pie_chart),
            dcc.Graph(figure=scatter_chart),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)
