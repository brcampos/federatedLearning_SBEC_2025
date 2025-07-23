
import pickle
import matplotlib.pyplot as plt

with open('modelo_global.pkl', 'rb') as f:
    modelo = pickle.load(f)

pesos = modelo['pesos']
variaveis = ['Frequência Cardíaca (bpm)', 'HRV (ms)']

plt.figure(figsize=(8, 5))
plt.bar(variaveis, pesos, color='darkorange')
plt.title('Coeficientes do Modelo Federado (Classificação de Risco)')
plt.ylabel('Peso')
plt.grid(True, axis='y')
plt.tight_layout()
plt.savefig('modelo_global_coeficientes.png')
plt.show()
