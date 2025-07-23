
import os
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

input_dir = 'data'
output_dir = 'modelos_cliente'
os.makedirs(output_dir, exist_ok=True)

for arquivo in os.listdir(input_dir):
    if arquivo.endswith('.csv'):
        df = pd.read_csv(os.path.join(input_dir, arquivo))
        X = df[['frequencia', 'hrv']]
        y = df['risco']

        if len(y.unique()) < 2:
            print(f"[AVISO] {arquivo} ignorado: apenas uma classe presente.")
            continue

        modelo = LogisticRegression()
        modelo.fit(X, y)

        resultado = {
            'pesos': modelo.coef_[0].tolist(),
            'intercepto': modelo.intercept_[0].item(),
            'n_amostras': len(y)
        }

        with open(os.path.join(output_dir, f'modelo_{arquivo}.pkl'), 'wb') as f:
            pickle.dump(resultado, f)

print("Modelos locais treinados com sucesso.")
