import pyautogui
import time
import random

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("notepad")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("Automacao funcionando!")

time.sleep(2)

pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write("cmd")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("echo Hello!")
pyautogui.press("enter")

time.sleep(5)

from playwright.sync_api import sync_playwright

PESQUISA = "gatos fofos"

with sync_playwright() as p:
    browser = p.chromium.launch(
        channel="msedge",
        headless=False
    )

    page = browser.new_page()

    # 1. Abre o YouTube
    page.goto("https://www.youtube.com")

    # 2. Localiza o campo de pesquisa
    pesquisa = page.locator("input[name='search_query']")

    # Espera o campo aparecer
    pesquisa.wait_for(state="visible")

    # 3. Preenche e pesquisa
    pesquisa.fill(PESQUISA)
    pesquisa.press("Enter")

    # 4. Espera os resultados
    page.wait_for_selector("ytd-video-renderer")

    # 5. Pega os vídeos
    videos = page.locator(
        "ytd-video-renderer a#video-title"
    )

    quantidade = videos.count()

    print(f"Encontrados {quantidade} vídeos.")

    if quantidade > 0:
        # 6. Escolhe um vídeo aleatório
        indice = random.randrange(quantidade)

        video = videos.nth(indice)

        # Mostra qual foi escolhido
        titulo = video.get_attribute("title")

        print(f"Vídeo escolhido: {titulo}")

        # 7. Espera 3 segundos
        page.wait_for_timeout(3000)

        # 8. Clica
        video.click()

        print("Vídeo aberto!")

    input("Pressione ENTER para fechar...")

    browser.close()

