from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import random
import time
import pickle
import os

# Function to login to Instagram
def login_instagram(username, password, driver):
    # Maximize the browser window
    driver.maximize_window()
    # Path to the cookies file
    cookies_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cookies.pkl")
    # Access the Instagram website
    driver.get("https://www.instagram.com/")
    # If cookies file exists, load the cookies
    if os.path.exists(cookies_file):
        with open(cookies_file, "rb") as file:
            cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
    time.sleep(5)
    # Try to handle notifications popup
    try:
        not_now_notifications_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Agora não"]')))
        not_now_notifications_btn.click()
    except TimeoutException:
        pass
    # Try to login
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        driver.find_element(By.NAME, 'username').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Try to handle save login info popup
        try:
            time.sleep(5)
            not_now_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Agora não")]')))
            not_now_btn.click()
        except TimeoutException:
            pass
        # Try to handle notifications popup
        try:
            time.sleep(5)
            not_now_notifications_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Agora não"]')))
            not_now_notifications_btn.click()
        except TimeoutException:
            pass
        # Dump cookies
        with open(cookies_file, "wb") as file:
            pickle.dump(driver.get_cookies(), file)
    except Exception as e:
        print(f"An error occurred while logging in: {e}")

# Function to comment on a post
def comment_on_post(post_url, base_comment, driver, num_comments):
    emoticons = [":)", ":D", ":P", "^^", ";)", "<3", ":]", ":3", ":>", "=)", "=]", "8)"]
    driver.get(post_url)
    time.sleep(10)
    for i in range(num_comments):
        base_comment = "".join(c.upper() if random.random() < 0.5 else c.lower() for c in base_comment)
        comment = base_comment + " " + random.choice(emoticons)
        comment_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Adicione um comentário..."]')
        comment_box.click()
        time.sleep(1)
        comment_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Adicione um comentário..."]')
        comment_box.send_keys(comment)
        time.sleep(1)
        post_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Publicar")]')))
        post_button.click()
        print(f"Comentário #{i + 1}: {comment} às {time.strftime('%H:%M:%S')}")
        # Pause for a random time between 50 and 70 seconds
        time.sleep(random.randint(50, 70))

# Main function
def main():
    # Instagram username and password
    username = 'username'
    password = 'password'
    # URL of the post to comment on
    post_url = 'https://www.instagram.com/p/CsUYwKJObqF/'
    # Base comment
    comment = 'EU QUERO'
    # Create options for the webdriver
    options = Options()
    # Set random user agent
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    # Path to the webdriver
    webdriver_service = Service('D:\pythonProject\botinstafuncionando\chromedriver_win32\chromedriver.exe')
    # Create webdriver
    driver = webdriver.Chrome(service=webdriver_service, options=options)

    try:
        # Login to Instagram
        login_instagram(username, password, driver)
        time.sleep(2)
        # Comment on post
        comment_on_post(post_url, comment, driver, 180)
        time.sleep(2)
    finally:
        # Quit driver
        driver.quit()

if __name__ == "__main__":
    main()

