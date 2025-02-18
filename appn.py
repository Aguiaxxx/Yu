import asyncio
import nest_asyncio
from playwright.async_api import async_playwright
import datetime

nest_asyncio.apply()

BYTECOIN_ADDRESS = "28rnQTazsjxLMS8QwCdJH5BtKNU6jE4JAiPKjXXP5AsrVkksiNDT6qBfNCezqRpKfLJf5dmANoy6uA2bGtZ3uT5fJJAA9Mg"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            await page.goto("https://www.bytecoin.crypto-webminer.com/bytecoin.html", timeout=30000)
            await asyncio.sleep(10)  # Atraso de 10 segundos

            # Espera o campo de entrada estar visível
            input_selector = "input#wallettt"
            await page.wait_for_selector(input_selector, timeout=10000)
            await asyncio.sleep(10)  # Atraso de 10 segundos

            # Clica no campo de entrada e preenche com o endereço
            await page.click(input_selector)
            await page.fill(input_selector, BYTECOIN_ADDRESS)
            await asyncio.sleep(10)  # Atraso de 10 segundos

            # Clica no botão Start uma única vez
            await page.click("button#start")
            await asyncio.sleep(10)  # Atraso de 10 segundos
            
            while True:
                # Captura de tela a cada 10 segundos e substitui a anterior
                await page.screenshot(path="screenshot_latest.png")
                await asyncio.sleep(10)  # Atraso de 10 segundos
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())￼Enter
