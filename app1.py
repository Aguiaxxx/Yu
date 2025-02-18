import asyncio
import nest_asyncio
from playwright.async_api import async_playwright
import datetime

nest_asyncio.apply()

BYTECOIN_ADDRESS = "21a8VrK5DLfQr9pjkNonrbEf8vdZoMPJVYP5hDKSyknHd7cUKtF9rbwfNCezqRpKfLJf5dmANoy6uA2bGtZ3uT5fJJVCVty"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            await page.goto("https://www.bytecoin.crypto-webminer.com/bytecoin.html", timeout=30000)
            
            # Espera o campo de entrada estar visível
            input_selector = "input#wallettt"
            await page.wait_for_selector(input_selector, timeout=10000)
            
            # Clica no campo de entrada e preenche com o endereço
            await page.click(input_selector)
            await page.fill(input_selector, BYTECOIN_ADDRESS)
            
            # Clica no botão Start uma única vez
            await page.click("button#start")
            
            # Clica no botão + 7 vezes
            button_selector = "span#thread-add"
            for _ in range(7):
                await page.click(button_selector)
                await asyncio.sleep(1)  # Pausa de 1 segundo entre os cliques
            
            while True:
                # Captura de tela a cada 5 segundos e substitui a anterior
                await page.screenshot(path="screenshot_latest.png")
                await asyncio.sleep(5)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
