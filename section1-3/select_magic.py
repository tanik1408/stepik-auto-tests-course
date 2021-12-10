from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector('#num1')
    num2 = browser.find_element_by_css_selector('#num2')
    summa = int(num1.text) + int(num2.text)
    print(summa)
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_css_selector('.custom-select'))
    select.select_by_value(str(summa))

    button = browser.find_element_by_css_selector("[type=submit]")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()