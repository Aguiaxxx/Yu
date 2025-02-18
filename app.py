
import asyncio
import nest_asyncio
from playwright.async_api import async_playwright
import datetime

nest_asyncio.apply()

BYTECOIN_ADDRESS = "24K8XW1GFRmbDsP2ho2mJSH9EJhJiJU7oBhoV9jaLcAM9WuV2h8mXTbfNCezqRpKfLJf5dmANoy6uA2bGtZ3uT5fJJPqXpZ"

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
