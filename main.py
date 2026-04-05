from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Calculadora API",
    description="API de Calculadora para Sistemas Distribuídos",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permite qualquer origem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class OperacaoRequest(BaseModel):
    numero1: float
    numero2: float

class ResultadoResponse(BaseModel):
    operacao: str
    numero1: float
    numero2: float
    resultado: float

@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à Calculadora API!", "docs": "/docs"}

@app.post("/somar", response_model=ResultadoResponse)
def somar(dados: OperacaoRequest):
    resultado = dados.numero1 + dados.numero2
    return ResultadoResponse(operacao="soma", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

@app.post("/subtrair", response_model=ResultadoResponse)
def subtrair(dados: OperacaoRequest):
    resultado = dados.numero1 - dados.numero2
    return ResultadoResponse(operacao="subtracao", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

@app.post("/multiplicar", response_model=ResultadoResponse)
def multiplicar(dados: OperacaoRequest):
    resultado = dados.numero1 * dados.numero2
    return ResultadoResponse(operacao="multiplicacao", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

@app.post("/dividir", response_model=ResultadoResponse)
def dividir(dados: OperacaoRequest):
    if dados.numero2 == 0:
        raise HTTPException(status_code=400, detail="Divisão por zero não é permitida!")
    resultado = dados.numero1 / dados.numero2
    return ResultadoResponse(operacao="divisao", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

@app.get("/calcular")
def calcular_query(numero1: float, numero2: float, operacao: str):
    operacoes = {
        "soma": lambda a, b: a + b,
        "subtracao": lambda a, b: a - b,
        "multiplicacao": lambda a, b: a * b,
        "divisao": lambda a, b: a / b,
    }
    if operacao not in operacoes:
        raise HTTPException(status_code=400, detail=f"Operação inválida. Use: {list(operacoes.keys())}")
    if operacao == "divisao" and numero2 == 0:
        raise HTTPException(status_code=400, detail="Divisão por zero!")
    return {"operacao": operacao, "numero1": numero1, "numero2": numero2, "resultado": operacoes[operacao](numero1, numero2)}
import math

@app.post("/potencia", response_model=ResultadoResponse)
def potencia(dados: OperacaoRequest):
    resultado = dados.numero1 ** dados.numero2
    return ResultadoResponse(operacao="potencia", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

@app.post("/raiz", response_model=ResultadoResponse)
def raiz(dados: OperacaoRequest):
    if dados.numero1 < 0:
        raise HTTPException(status_code=400, detail="Não é possível calcular raiz de número negativo!")
    resultado = math.sqrt(dados.numero1)
    return ResultadoResponse(operacao="raiz", numero1=dados.numero1, numero2=0, resultado=resultado)
