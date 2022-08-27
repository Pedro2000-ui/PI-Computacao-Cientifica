import numpy as np

# Carrega os arquivos altura.txt e anos.txt e armazena os dados nas variáveis 
alturas = np.loadtxt('altura.txt')
anos = np.loadtxt('anos.txt')

# Armazena os índices dos dados que se encontram na variável "anos" dentro do intervalo estipulado
idxAnos = np.where((anos >= 1998) & (anos <= 2005))
# Retorna o tamanho da lista contando apenas onde os valores estão dentro do intervalo estipulado
tamanho = len(anos[idxAnos])
soma = 0;

# Soma todas as alturas que correspondem aos índices armazenados
for item in alturas[idxAnos]:
  soma += item;

#Calcula a média e armazena com apenas duas casas após a vírgula 
media = round(soma / tamanho, 2)
print("Média de altura: " + str(media) + " metros")
