
# 🧠 Aplicação de Aprendizado Federado com Wearables (Frequência Cardíaca + HRV)

Esta aplicação simula um cenário industrial onde três dispositivos vestíveis monitoram a frequência cardíaca (FC) e a variabilidade da frequência cardíaca (HRV) de operadores. Os dados são processados localmente e apenas os parâmetros do modelo são enviados ao servidor central. Isso garante privacidade e atende à LGPD.

---

## 📁 Estrutura do Projeto

```
nova_aplicacao_fc_hrv/
├── client.py               # Treina modelos locais para cada wearable
├── server.py               # Agrega os modelos via FedAvg
├── plot_modelo.py          # Gera gráfico com os coeficientes do modelo global
├── modelo_global.pkl       # Modelo global treinado
├── modelo_global_coeficientes.png  # Gráfico com pesos do modelo global
├── modelos_cliente/        # Modelos locais por cliente
├── data/
│   ├── dispositivo_1.csv
│   ├── dispositivo_2.csv
│   └── dispositivo_3.csv
└── README.md
```

---

## ▶️ Como Executar

### 1. Treinar modelos locais
```bash
python client.py
```

### 2. Agregar modelo global com FedAvg
```bash
python server.py
```

### 3. Visualizar os coeficientes aprendidos
```bash
python plot_modelo.py
```

---

## 💾 Dados de Entrada

Localizados em `data/`, os arquivos CSV devem conter:

- `frequencia`: frequência cardíaca em bpm
- `hrv`: variabilidade da frequência cardíaca em ms
- `risco`: 0 = normal, 1 = risco

---

## ⚙️ Requisitos

- Python 3.x
- `scikit-learn`
- `matplotlib`
- `pandas`
- `numpy`

Instale com:

```bash
pip install -r requirements.txt
```

---

## 📌 Modelo

- Regressores locais: `LogisticRegression`
- Agregação: `FedAvg` ponderado por número de amostras
- Interpretável: gráfico com os pesos mostra influência de FC e HRV

---

## 🔒 Privacidade

Nenhum dado bruto é enviado ao servidor. A arquitetura preserva a confidencialidade dos sinais fisiológicos dos trabalhadores.

---

## 🧪 Uso Acadêmico

Este exemplo foi criado para apoiar submissões científicas sobre Aprendizado Federado com wearables em ambientes industriais.
