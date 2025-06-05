import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helper.url import main_url, order_url, dzen
from pages.ordering_scooter_pages import OrderingScooter
from locators.ordering_scooter_locators import MainScooterLocators, OrderingScooterLocators, OrderSuccessfullyPlacedLocators
from helper.test_data import user_data_1, user_data_2


main_scooter_locators = MainScooterLocators()
ordering_scooter_locators = OrderingScooterLocators()
ordering_scooter = OrderingScooter()
order_successfully_placed_locators = OrderSuccessfullyPlacedLocators()


class TestOrderingScooter:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Тест успешного заказа самоката при нажатии кнопки "Заказать" вверху главной страницы')
    def test_successful_scooter_order_button_order_on_top(self):
        # Перейти на главную страницу сайта
        self.driver.get(main_url)

        # Нажать кнопку "Заказать" вверху главной страницы
        ordering_scooter.click_button_order_on_top(self.driver)

        # Выбор объекта с данными для заполнения полей заказа самоката
        user_data = user_data_1

        # Заполнение полей для заказа на страницах "Для кого самокат", "Про аренду", "Хотите оформить заказ"
        ordering_scooter.filling_order_fields(self.driver, user_data)

        # Проверка, что заказ оформлен успешно (отображается окно "Заказ оформлен")
        order_confirmation = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                                                 (order_successfully_placed_locators.order_successfully_placed))
        assert "Заказ оформлен" in order_confirmation.text


    @allure.title('Тест успешного заказа самоката при нажатии кнопки "Заказать" внизу главной страницы')
    def test_successful_scooter_order_button_order_below(self):
        # Перейти на главную страницу сайта
        self.driver.get(main_url)

        # Нажать кнопку "Заказать" внизу главной страницы
        ordering_scooter.click_button_order_below(self.driver)

        # Выбор объекта с данными для заполнения полей заказа самоката
        user_data = user_data_2

        # Заполнение полей для заказа на страницах "Для кого самокат", "Про аренду", "Хотите оформить заказ"
        ordering_scooter.filling_order_fields(self.driver, user_data)

        # Проверка, что заказ оформлен успешно (отображается окно "Заказ оформлен")
        order_confirmation = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(order_successfully_placed_locators.order_successfully_placed))
        assert "Заказ оформлен" in order_confirmation.text


    @allure.title('Тест успешного перехода на главную страницу при нажатии на логотип «Самоката»')
    def test_successful_go_to_main_page_via_logo_scooter(self):
        # Перейти на страницу заказа самоката
        self.driver.get(order_url)

        self.driver.find_element(*ordering_scooter_locators.scooter_logo_order).click()

        assert self.driver.current_url == main_url


    @allure.title('Тест успешного перехода на главную страницу Дзена при нажатии на логотип Яндекса')
    def test_successful_go_to_dzen_page_via_logo_yandex(self):
        # Перейти на страницу заказа самоката
        self.driver.get(order_url)

        # Нажать на логотип Яндекса
        logo_yandex = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(main_scooter_locators.yandex_logo_order))
        logo_yandex.click()

        # Переключиться на новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # Дождаться, пока в адресной строке появится адрес Дзен
        WebDriverWait(self.driver, 15).until(expected_conditions.url_contains(dzen))

        # Проверка, что адрес открывшейся страницы - главная страница Дзена
        assert self.driver.current_url == dzen


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

