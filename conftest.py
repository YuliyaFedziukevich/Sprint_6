import pytest
from selenium import webdriver
from helper.url import main_url, order_url


# Открытие/закрытие главной страницы
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(main_url)

    yield driver

    driver.quit()

# Открытие/закрытие страницы заказа
@pytest.fixture(scope="function")
def driver_order():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(order_url)

    yield driver

    driver.quit()


