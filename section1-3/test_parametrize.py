import pytest
from selenium import webdriver
import time
import math

final_text = ''
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    print('Answer for lesson:' + final_text)
    browser.quit()

@pytest.mark.parametrize('pytest', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_guest_should_see_login_link(browser, pytest):
    link = f"https://stepik.org/lesson/{pytest}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    input1 = browser.find_element_by_class_name('ember-text-area')
    answer = math.log(int(time.time()))
    input1.send_keys(answer)
    button = browser.find_element_by_class_name('submit-submission')
    button.click()
    browser.implicitly_wait(5)
    text = browser.find_element_by_class_name('smart-hints__feedback').text
    global final_text
    if text != 'Correct!':
        final_text += text
    assert text == 'Correct!', f"wrong answer in lesson {pytest}"