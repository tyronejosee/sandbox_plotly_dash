import pandas as pd

from .constants import (
    SHEET_NAME,
    COLUMNAS_NECESARIAS,
    COLUMNA_ABONOS,
    COLUMNA_CARGOS,
    COLUMNA_FICHA,
)


def process_excel(input_file) -> pd.DataFrame:
    try:
        df: pd.DataFrame = pd.read_excel(
            input_file,
            sheet_name=SHEET_NAME,
        )
    except ValueError as e:
        print(f"Error leyendo el archivo Excel: {e}")
        return pd.DataFrame()

    if not all(col in df.columns for col in COLUMNAS_NECESARIAS):
        print(f"Faltan columnas necesarias: {COLUMNAS_NECESARIAS}")
        return pd.DataFrame()

    for col in [COLUMNA_ABONOS, COLUMNA_CARGOS]:
        df[col] = df[col].replace({",": ""}, regex=True)
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=[COLUMNA_FICHA, COLUMNA_ABONOS, COLUMNA_CARGOS])

    grouped: pd.DataFrame = df.groupby(COLUMNA_FICHA).agg(
        {COLUMNA_ABONOS: "sum", COLUMNA_CARGOS: "sum"}
    )
    grouped.index = grouped.index.str.split().str[0:2].str.join(" ")
    return grouped
