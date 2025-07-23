
import os
import pickle
import numpy as np

input_dir = 'modelos_cliente'
modelos = []

for arquivo in os.listdir(input_dir):
    if arquivo.endswith('.pkl'):
        with open(os.path.join(input_dir, arquivo), 'rb') as f:
            modelos.append(pickle.load(f))

if not modelos:
    raise ValueError("Nenhum modelo foi encontrado para agregação.")

pesos = np.array([m['pesos'] for m in modelos])
interceptos = np.array([m['intercepto'] for m in modelos])
n_amostras = np.array([m['n_amostras'] for m in modelos])

pesos_global = np.average(pesos, axis=0, weights=n_amostras)
intercepto_global = np.average(interceptos, weights=n_amostras)

modelo_global = {
    'pesos': pesos_global,
    'intercepto': intercepto_global
}

with open('modelo_global.pkl', 'wb') as f:
    pickle.dump(modelo_global, f)

print("Modelo global salvo com sucesso.")
