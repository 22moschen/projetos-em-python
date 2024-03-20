from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Abre o Instagram
driver.get("https://www.instagram.com/")

# Espera um tempo antes de executar o bot
time.sleep(5)

# Localiza e preenche o campo de usuário
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("teste")

# Localiza e preenche o campo de senha
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("teste")

# Pressiona Enter para fazer login
password_field.send_keys(Keys.ENTER)

# Espera o login ser concluído
time.sleep(5)

# Insira o link do post do Instagram
post_url = "https://www.instagram.com/p/CrBeYPaL7xF/?utm_source=ig_web_copy_link"

# Número de vezes que você deseja comentar
num_comments = 5

# Loop para comentar várias vezes
for _ in range(num_comments):
    # Abre o post
    driver.get(post_url)

    # Espera um tempo antes de executar o bot
    time.sleep(5)

    # Localiza e preenche o campo de comentário
    comment_input = driver.find_element(By.CSS_SELECTOR, "textarea.Ypffh")
    comment_input.send_keys("eu quero")

    # Encontra o botão de enviar
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Espera um tempo antes de comentar novamente
    time.sleep(5)

# Fecha o navegador
driver.quit()
