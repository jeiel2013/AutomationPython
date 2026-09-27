import os
import shutil

pasta = "Arquivos"
itens = os.listdir(pasta)

for item in itens:
    caminho_origem = os.path.join(pasta, item)
    
    if not os.path.isfile(caminho_origem):
        continue
        
    nome, extensao = os.path.splitext(item)
    
    if not extensao:
        continue 
        
    extensaoUp = extensao.replace(".", "").upper()
    caminho_destino = os.path.join(pasta, extensaoUp)

    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)
        print(f"Pasta {extensaoUp} adicionada!")

    caminho_arquivo_destino = os.path.join(caminho_destino, item)
    
    shutil.move(caminho_origem, caminho_arquivo_destino)
    print(f"Arquivo '{item}' movido para '{extensaoUp}'")