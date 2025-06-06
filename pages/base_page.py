from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Поиск элемента
    def find(self, locators):
        return self.driver.find_element(*locators)

    # Кликнуть найденный элемент
    def click(self, locators):
        self.find(locators).click()

    # Заполнение поля данными
    def send_keys(self, locators, data):
        self.find(locators).send_keys(data)

    # Получить текст элемента
    def text(self, locators):
        return self.find(locators).text

    # Дождаться, пока элемент будет кликабельным
    def wait_clickable(self, locators):
        return self.wait.until(expected_conditions.element_to_be_clickable(locators))

    # Дождаться, пока элемент будет кликабельным, и кликнуть его
    def wait_clickable_and_click(self, locators):
        return self.wait_clickable(locators).click()

    # Дождаться, пока элемент будет видимым
    def wait_visibility(self, locators):
        return self.wait.until(expected_conditions.visibility_of_element_located(locators))

    # Дождаться, пока в адресной строке появится адрес
    def wait_url_contains(self, data):
        return self.wait.until(expected_conditions.url_contains(data))

    # Перейти к вопросу (с использованием прокрутки)
    def scroll(self, locators):
        element = self.find(locators)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        return element

    # Переключиться на новую вкладку
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def current_url(self):
        return self.driver.current_url



