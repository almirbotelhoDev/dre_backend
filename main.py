from fastapi import FastAPI, UploadFile, File
import pandas as pd
from services.dre_service import processar_dre

# 👇 PRIMEIRO define o app
app = FastAPI()

# 👇 DEPOIS cria a rota
@app.post("/process")
async def process(file: UploadFile = File(...)):

    print("Recebendo arquivo...")
    
    df = pd.read_excel(file.file)
    print("Arquivo carregado")

    df["Data"] = pd.to_datetime(df["Data"])

    resultado = processar_dre(df)

    print("Processamento concluído")

    return resultado
