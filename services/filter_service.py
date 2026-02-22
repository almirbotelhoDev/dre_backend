def apply_filters(df, filters):

    if filters.start_date:
        df = df[df["Data"] >= filters.start_date]

    if filters.end_date:
        df = df[df["Data"] <= filters.end_date]

    if filters.centro_custo:
        df = df[df["Centro de Custo"] == filters.centro_custo]

    if filters.categoria:
        df = df[df["Categoria"] == filters.categoria]

    return df