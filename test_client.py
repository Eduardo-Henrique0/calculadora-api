import urllib.request, json

BASE_URL = "http://localhost:8000"

def post(endpoint, dados):
    req = urllib.request.Request(
        f"{BASE_URL}{endpoint}",
        data=json.dumps(dados).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

# Testes
print("Soma:", post("/somar", {"numero1": 10, "numero2": 5})["resultado"])          # 15
print("Subtração:", post("/subtrair", {"numero1": 10, "numero2": 3})["resultado"])  # 7
print("Multiplicação:", post("/multiplicar", {"numero1": 4, "numero2": 5})["resultado"])  # 20
print("Divisão:", post("/dividir", {"numero1": 10, "numero2": 2})["resultado"])     # 5
print("Potência:", post("/potencia", {"numero1": 2, "numero2": 3})["resultado"])  # 8
print("Raiz:", post("/raiz", {"numero1": 9, "numero2": 0})["resultado"])          # 3

