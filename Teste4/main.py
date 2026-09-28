import os
from collections import Counter

pasta = input("Informe o caminho da pasta a ser analisada: ")

total_arquivos = 0
total_pastas = 0

# 1. Cria o contador vazio ANTES do loop
contagem = Counter() 

if not os.path.exists(pasta):
    print("Pasta não encontrada.")
    exit()

print(f"Analisando {pasta}...\n")

for item in os.scandir(pasta):
    if item.is_dir():
        total_pastas += 1
        
    elif item.is_file():
        total_arquivos += 1
        
        nome, extensao = os.path.splitext(item.name)
        
        if extensao:
            contagem[extensao.lower()] += 1 
        else:
            contagem["Sem extensão"] += 1
            
print(f"Total de pastas: {total_pastas}")
print(f"Total de arquivos: {total_arquivos}")
print("\n--- Extensões ---")

for extensao, quantidade in contagem.items():
    print(f"{extensao}: {quantidade}")