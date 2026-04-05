 📘 Calculadora API

API desenvolvida em **FastAPI** para realizar operações matemáticas básicas e intermediárias.  
Projeto avaliativo da disciplina **Programação de Sistemas Distribuídos** da **Universidade do Grandes Lagos - UNILAGO**, sob supervisão do Professor: https://github.com/gleydes.

---

 🚀 Funcionalidades
- ➕ Somar  
- ➖ Subtrair  
- ✖️ Multiplicar  
- ➗ Dividir (com tratamento de divisão por zero)  
- 🔼 Potência  
- √ Raiz quadrada (com tratamento de número negativo)  

---

 📂 Estrutura do projeto
  calculadora-api/
├── main.py            # API FastAPI
├── requirements.txt   # Dependências
├── test_client.py     # Script de testes
├── frontend/
│   └── index.html     # Interface web
└── README.md          # Documentação


---

⚙️ Como rodar
1. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   python -m uvicorn main:app --reload
   http://127.0.0.1:8000/docs


    
