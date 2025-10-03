import time
import logging.config

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

logging.config.fileConfig("logging.conf")
logger =logging.getLogger()


driver = Chrome() # ініціалізація веб драйвера

driver.get("http://localhost:8000/dz.html") # запуск драйвера і відкриття сторінки

frame_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "frame1")))
driver.switch_to.frame(frame_1)
time.sleep(1)

input_1 = driver.find_element(By.ID, "input1")
input_1.click()
time.sleep(1)
input_1.send_keys("Frame1_Secret")
time.sleep(1)

button = driver.find_element(By.XPATH, "html/body/button")
button.click()
time.sleep(1)

alert = driver.switch_to.alert
time.sleep(1)

for text in alert.text.splitlines():
    if text != "Верифікація пройшла успішно!":
        print('Тексти на співпадають')
        logger.warning(f"Текст <<{text}>> не співпав з текстом <<Верифікація пройшла успішно!>> ")
        break
    else:
        alert.accept()
        logger.info("Перший фрейм успішно пройдено!")

input_1 = driver.find_element(By.ID, "input1")
input_1.clear()

driver.switch_to.default_content()

frame_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "frame2")))
driver.switch_to.frame(frame_2)

input_2 = driver.find_element(By.ID, "input2")
input_2.click()
time.sleep(1)
input_2.send_keys("Frame2_Secret")
time.sleep(1)

button = driver.find_element(By.XPATH, "html/body/button")

button.click()
time.sleep(1)

alert = driver.switch_to.alert
time.sleep(1)

for text in alert.text.splitlines():
    if text != "Верифікація пройшла успішно!":
        print('Тексти на співпадають')
        logger.warning(f"Текст <<{text}>> не співпав з текстом <<Верифікація пройшла успішно!>> ")
        break
    else:
        alert.accept()
        logger.info("Другий фрейм успішно пройдено!")

input_2 = driver.find_element(By.ID, "input2")
input_2.clear()

driver.switch_to.default_content()

time.sleep(1)
driver.quit()

