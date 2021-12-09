from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_css_selector('#treasure')
    x = treasure.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    check1 = browser.find_element_by_css_selector('#robotCheckbox')
    check1.click()

    radio1 = browser.find_element_by_css_selector('#robotsRule')
    radio1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type=submit]")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()