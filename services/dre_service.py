import pandas as pd

def processar_dre(df):

    df["Data"] = pd.to_datetime(df["Data"])
    df["Mes"] = df["Data"].dt.to_period("M").astype(str)

    receita_total = df[df["Tipo"] == "Receita"]["Valor"].sum()
    despesa_total = df[df["Tipo"] == "Despesa"]["Valor"].sum()

    lucro = receita_total - despesa_total
    margem = (lucro / receita_total * 100) if receita_total != 0 else 0

    evolucao = (
        df.groupby("Mes")
        .apply(lambda x:
            x[x["Tipo"] == "Receita"]["Valor"].sum() -
            x[x["Tipo"] == "Despesa"]["Valor"].sum()
        )
        .reset_index(name="Lucro")
    )

    return {
        "dados": df.to_dict(orient="records"),
        "receita_total": float(receita_total),
        "despesa_total": float(despesa_total),
        "lucro": float(lucro),
        "margem": float(margem),
        "evolucao": evolucao.to_dict(orient="records")
    }