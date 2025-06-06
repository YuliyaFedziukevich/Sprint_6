import allure
from helper.url import main_url, dzen
from pages.ordering_scooter_pages import OrderingScooter
from locators.ordering_scooter_locators import MainScooterLocators, OrderingScooterLocators, OrderSuccessfullyPlacedLocators
from helper.test_data import user_data_1, user_data_2, successful_message


main_scooter_locators = MainScooterLocators()
ordering_scooter_locators = OrderingScooterLocators()
order_successfully_placed_locators = OrderSuccessfullyPlacedLocators()


class TestOrderingScooter:


    @allure.title('Тест успешного заказа самоката при нажатии кнопки "Заказать" вверху главной страницы')
    def test_successful_scooter_order_button_order_on_top(self, driver):

        ordering_scooter = OrderingScooter(driver)

        # Нажать кнопку "Заказать" вверху главной страницы
        ordering_scooter.click_button_order_on_top()

        # Выбор объекта с данными для заполнения полей заказа самоката
        user_data = user_data_1

        # Заполнение полей для заказа на страницах "Для кого самокат", "Про аренду", "Хотите оформить заказ"
        ordering_scooter.filling_order_fields(user_data)

        # Проверка, что заказ оформлен успешно (отображается окно "Заказ оформлен")
        order_confirmation = ordering_scooter.wait_visibility(order_successfully_placed_locators.order_successfully_placed)

        assert successful_message in order_confirmation.text


    @allure.title('Тест успешного заказа самоката при нажатии кнопки "Заказать" внизу главной страницы')
    def test_successful_scooter_order_button_order_below(self, driver):

        ordering_scooter = OrderingScooter(driver)

        # Нажать кнопку "Заказать" внизу главной страницы
        ordering_scooter.click_button_order_below()

        # Выбор объекта с данными для заполнения полей заказа самоката
        user_data = user_data_2

        # Заполнение полей для заказа на страницах "Для кого самокат", "Про аренду", "Хотите оформить заказ"
        ordering_scooter.filling_order_fields(user_data)

        # Проверка, что заказ оформлен успешно (отображается окно "Заказ оформлен")
        order_confirmation = ordering_scooter.wait_visibility(order_successfully_placed_locators.order_successfully_placed)

        assert successful_message in order_confirmation.text


    @allure.title('Тест успешного перехода на главную страницу при нажатии на логотип «Самоката»')
    def test_successful_go_to_main_page_via_logo_scooter(self, driver_order):
        ordering_scooter = OrderingScooter(driver_order)

        # Нажать на логотип "Самоката"
        ordering_scooter.click(ordering_scooter_locators.scooter_logo_order)

        # Проверка, что адрес открывшейся страницы - главная страница
        assert ordering_scooter.current_url() == main_url


    @allure.title('Тест успешного перехода на главную страницу Дзена при нажатии на логотип Яндекса')
    def test_successful_go_to_dzen_page_via_logo_yandex(self, driver_order):
        ordering_scooter = OrderingScooter(driver_order)

        # Нажать на логотип Яндекса
        ordering_scooter.wait_clickable_and_click(main_scooter_locators.yandex_logo_order)

        # Переключиться на новую вкладку
        ordering_scooter.switch_to_last_window()

        # Дождаться, пока в адресной строке появится адрес Дзен
        ordering_scooter.wait_url_contains(dzen)

        # Проверка, что адрес открывшейся страницы - главная страница Дзена
        assert ordering_scooter.current_url() == dzen
