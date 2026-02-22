import pandas as pd

def read_excel(file):
    df = pd.read_excel(file)

    required_columns = ["Data", "Categoria", "Tipo", "Centro de Custo", "Valor"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Coluna obrigatória não encontrada: {col}")

    df["Data"] = pd.to_datetime(df["Data"])
    df["Valor"] = pd.to_numeric(df["Valor"])

    return df