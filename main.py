from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from services.dre_service import processar_dre

app = FastAPI()

# Adicionar isso:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 DEPOIS cria a rota
@app.post("/process")
async def process(file: UploadFile = File(...)):

    print("Recebendo arquivo...")
    
    df = pd.read_excel(file.file)
    print("Arquivo carregado")

    print("Colunas recebidas:", df.columns.tolist())
    
    df["Data"] = pd.to_datetime(df["Data"])

    resultado = processar_dre(df)

    print("Processamento concluído")

    return resultado
