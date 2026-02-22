class DREModel:
    def __init__(self, df):
        self.df = df

    def receita_bruta(self):
        return self.df[self.df["Tipo"] == "Receita"]["Valor"].sum()

    def despesas(self):
        return self.df[self.df["Tipo"] == "Despesa"]["Valor"].sum()

    def lucro(self):
        return self.receita_bruta() - self.despesas()

    def margem(self):
        receita = self.receita_bruta()
        return (self.lucro() / receita) * 100 if receita != 0 else 0