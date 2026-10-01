import pandas as pd
import time
import os
from playwright.sync_api import sync_playwright
from pathlib import Path

pasta_home = Path.home()
pasta_downloads = pasta_home / "Downloads"

caminho_arquivo = r"clientes.xlsx"
tabela = pd.read_excel(caminho_arquivo)

tabela['CNPJ'] = tabela['CNPJ'].astype(str)
tabela['SENHA'] = tabela['SENHA'].astype(str)
lista_empresas = tabela[['CNPJ', 'LOGIN', 'SENHA']].to_dict(orient='records')

competencia = input("Informe a Competência desejada (MM/AAAA): ")

nome_da_pasta = pasta_downloads / str(competencia).replace("/", "-")

with sync_playwright() as p:
    browser = p.chromium.launch(
        channel="msedge",
        headless=False
    )
    
    for empresa in lista_empresas:
        cnpj_atual = empresa['CNPJ']
        usuario_atual = empresa['LOGIN']
        senha_atual = empresa['SENHA']
        
        print(f"Iniciando acesso para {usuario_atual} (CNPJ: {cnpj_atual})")
        
        page = browser.new_page()
        
        try:
            page.goto("https://coroacimg.futurize-nfse.com.br/canalprestador.php")
            
            time.sleep(2)
            
            page.fill("id=pst_cpfcnpj", cnpj_atual)
            page.fill("id=usu_login", usuario_atual)
            page.fill("id=usu_senha", senha_atual)
            
            page.click("#btnsubmitwait") 
            
            page.wait_for_load_state("networkidle")
            
            time.sleep(3)
            
            page.goto("https://coroacimg.futurize-nfse.com.br/listanotasfiscais_pst.php")
            
            time.sleep(2)
            
            page.fill("id=competencia", str(competencia))
            page.locator("select[name='snf_codigo']").select_option(value="1")
            page.locator("select[name='numregistros']").select_option(value="0")
            
            time.sleep(2)
            
            page.click("#btnfiltrogrid")
            
            time.sleep(4)
            
            if not os.path.exists(nome_da_pasta):
                os.makedirs(nome_da_pasta)
            
            with page.expect_download() as download_info:
                page.click("#btndownlistnfse2")
                
            download = download_info.value

            nome_arquivo = usuario_atual + os.path.splitext(download.suggested_filename)[1]
            caminho_final = os.path.join(nome_da_pasta, nome_arquivo)
            
            download.save_as(caminho_final)
            
            print(f"Arquivo baixado e salvo com sucesso em: {caminho_final}")
            
            time.sleep(8)
            
            print(f"Sucesso ao processar a empresa {cnpj_atual}")
            time.sleep(2)
            
        except Exception as e:
            print(f"Erro ao tentar processar o CNPJ {cnpj_atual}: {e}")
            
        finally:
            page.close()
            print(f"Aba finalizada para: {cnpj_atual}")
            print("-" * 40)
            
    browser.close()
    print("Processo finalizado!")
