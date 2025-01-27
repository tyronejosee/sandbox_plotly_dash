from typing import Any
import plotly.graph_objects as go
from pandas import DataFrame, Series, Index

from .constants import COLUMNA_ABONOS, COLUMNA_CARGOS


def create_bar_chart(dataframe: DataFrame) -> go.Figure:
    fichas: Index = dataframe.index
    abonos: Series = dataframe[COLUMNA_ABONOS]
    cargos: Series = dataframe[COLUMNA_CARGOS]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=fichas,
            y=abonos,
            name="Abonos",
            marker_color="skyblue",
        )
    )
    fig.add_trace(
        go.Bar(
            x=fichas,
            y=cargos,
            name="Cargos",
            marker_color="lightcoral",
            base=abonos,
        )
    )

    fig.update_layout(
        title="Totales de Abonos y Cargos por Ficha",
        xaxis_title="Ficha",
        yaxis_title="Monto Total",
        barmode="stack",
        xaxis_tickangle=-45,
        template="plotly_white",
        showlegend=True,
    )
    return fig


def create_line_chart(dataframe: DataFrame) -> go.Figure:
    fichas: Index = dataframe.index
    abonos: Series = dataframe[COLUMNA_ABONOS]
    cargos: Series = dataframe[COLUMNA_CARGOS]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=fichas,
            y=abonos,
            mode="lines+markers",
            name="Abonos",
            line=dict(color="skyblue"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=fichas,
            y=cargos,
            mode="lines+markers",
            name="Cargos",
            line=dict(color="lightcoral"),
        )
    )

    fig.update_layout(
        title="Evolución de Abonos y Cargos por Ficha",
        xaxis_title="Ficha",
        yaxis_title="Monto Total",
        template="plotly_white",
        showlegend=True,
    )
    return fig


def create_pie_chart(dataframe: DataFrame) -> go.Figure:
    total_abonos = dataframe[COLUMNA_ABONOS].sum()
    total_cargos = dataframe[COLUMNA_CARGOS].sum()

    labels: list[str] = ["Abonos", "Cargos"]
    values: list[Any] = [total_abonos, total_cargos]

    fig = go.Figure()
    fig.add_trace(
        go.Pie(
            labels=labels,
            values=values,
            marker=dict(
                colors=["skyblue", "lightcoral"],
            ),
        )
    )

    fig.update_layout(
        title="Proporción de Abonos y Cargos Totales",
        template="plotly_white",
        showlegend=True,
    )
    return fig


def create_scatter_chart(dataframe: DataFrame) -> go.Figure:
    abonos: Series = dataframe[COLUMNA_ABONOS]
    cargos: Series = dataframe[COLUMNA_CARGOS]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=abonos,
            y=cargos,
            mode="markers",
            name="Abonos vs Cargos",
        )
    )

    fig.update_layout(
        title="Comparación entre Abonos y Cargos",
        xaxis_title="Abonos",
        yaxis_title="Cargos",
        template="plotly_white",
        showlegend=True,
    )
    return fig
