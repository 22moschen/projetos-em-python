import time
import pyautogui
import random
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By


def bot():
    caixatexto = pyautogui.locateOnScreen('caixatexto.png')
    if caixatexto is not None:
        # Coordenadas da caixa de texto encontrada
        x, y, largura, altura = caixatexto

        # Clica na caixa de texto
        pyautogui.click(x + largura // 2, y + altura // 2)

        # Preenche o texto a ser digitado
        texto = "eu quero"
        pyperclip.copy(texto)
        pyautogui.hotkey("ctrl", "v")

        # Pressiona Enter para enviar o comentário
        pyautogui.press("enter")

        # Aguarda um tempo antes de executar novamente
        time.sleep(5)

    else:
        print("Caixa de texto não encontrada.")


# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Abre o Instagram
driver.get("https://www.instagram.com/")
time.sleep(5)

# Localiza e preenche o campo de usuário
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Murilo.moschen")

# Localiza e preenche o campo de senha
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("adedonha98765")

# Localiza e clica no botão de login
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Aguarda o login ser concluído
time.sleep(5)

# Insira o link do post do Instagram
post_url = "https://www.instagram.com/p/CsUYwKJObqF/?utm_source=ig_web_copy_link&igshid=MmJiY2I4NDBkZg=="

# Navega para o post
driver.get(post_url)

# Espera um tempo antes de executar o bot
time.sleep(5)

# Executa o bot
bot()

# Fecha o navegador
driver.quit()

