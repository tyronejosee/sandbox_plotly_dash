import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

# Datos de ejemplo
data = {
    "Ficha": [
        "50.340.420-6",
        "52.005.017-5",
        "52.005.017-5",
        "52.005.017-5",
        "70.285.100-9",
    ],
    "Fecha": ["05/05/2024", "20/12/2023", "31/10/2024", "31/10/2024", "20/11/2024"],
    "Tipo Doc.": [
        "Factura Electrónica",
        "Factura Electrónica",
        "Factura Electrónica",
        "Factura Electrónica",
        "Factura Electrónica",
    ],
    "Abonos $": [131876, 1062865, 1, 0, 0],
    "Cargos $": [0, 1062865, 0, 1, 53834],
    "Saldo $": [-131876, 0, -1, 1, 53834],
}

df = pd.DataFrame(data)

# Inicializar la aplicación Dash
app = dash.Dash(__name__)


# Gráfico de abonos y cargos por ficha
def crear_grafico_abonos_cargos(df):
    fig = go.Figure()

    for ficha in df["Ficha"].unique():
        df_ficha = df[df["Ficha"] == ficha]
        fig.add_trace(
            go.Bar(
                x=df_ficha["Ficha"],
                y=df_ficha["Abonos $"],
                name=f"{ficha} Abonos",
                marker_color="skyblue",
            )
        )
        fig.add_trace(
            go.Bar(
                x=df_ficha["Ficha"],
                y=df_ficha["Cargos $"],
                name=f"{ficha} Cargos",
                marker_color="lightcoral",
            )
        )

    fig.update_layout(
        title="Abonos y Cargos por Ficha",
        barmode="stack",
        xaxis_title="Ficha",
        yaxis_title="Monto ($)",
        template="plotly_dark",  # Usar fondo claro predeterminado de Plotly
    )
    return fig


# Gráfico de saldo a lo largo del tiempo
def crear_grafico_saldo(df):
    fig = go.Figure()

    for ficha in df["Ficha"].unique():
        df_ficha = df[df["Ficha"] == ficha]
        fig.add_trace(
            go.Scatter(
                x=df_ficha["Fecha"],
                y=df_ficha["Saldo $"],
                mode="lines+markers",
                name=f"Saldo {ficha}",
            )
        )

    fig.update_layout(
        title="Saldo a lo largo del tiempo por Ficha",
        xaxis_title="Fecha",
        yaxis_title="Saldo ($)",
        template="plotly",  # Usar fondo claro predeterminado de Plotly
    )
    return fig


# Crear el layout de la aplicación
app.layout = html.Div(
    [
        html.H1("Dashboard"),
        dcc.Graph(id="grafico-abonos-cargos", figure=crear_grafico_abonos_cargos(df)),
        dcc.Graph(id="grafico-saldo", figure=crear_grafico_saldo(df)),
    ],
    style={
        "margin": "0 auto",
        "paddingLeft": "40px",
        "paddingRight": "40px",
    },
)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)
