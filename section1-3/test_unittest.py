from selenium import webdriver
import unittest
import time

class TestAbs(unittest.TestCase):
    def test_1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element_by_css_selector('.first_block .first')
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector('.first_block .second')
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector('.first_block .third')
            input3.send_keys("email")
            input4 = browser.find_element_by_css_selector('.second_block div:first-child input')
            input4.send_keys("79000000000")
            input5 = browser.find_element_by_css_selector('.second_block div:last-child input')
            input5.send_keys("Moscow")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
    def test_2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element_by_css_selector('.first_block .first')
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector('.first_block .second')
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector('.first_block .third')
            input3.send_keys("email")
            input4 = browser.find_element_by_css_selector('.second_block div:first-child input')
            input4.send_keys("79000000000")
            input5 = browser.find_element_by_css_selector('.second_block div:last-child input')
            input5.send_keys("Moscow")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                             "Should be absolute value of a number")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()

