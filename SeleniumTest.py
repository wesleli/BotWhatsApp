from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



navegador = webdriver.Chrome()

navegador.get("https://ri.magazineluiza.com.br/")

navegador.find_element(By.XPATH, '//*[@id="slick-slide10"]/div/div/div/div/div/div/a').click()

