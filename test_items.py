import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    basket=browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(basket)>0, 'Элемент не найден'