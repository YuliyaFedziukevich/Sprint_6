import allure
from pages.ordering_scooter_pages import OrderingScooter


class TestOrderingScooter:

    @allure.title('Тест успешного заказа самоката при нажатии кнопки "Заказать" вверху главной страницы')
    def test_successful_scooter_order_button_order_on_top(self, driver):

        ordering_scooter = OrderingScooter(driver)

        # Нажать кнопку "Заказать" вверху главной страницы
        ordering_scooter.click_button_order_on_top()

        # Заполнение полей для заказа на страницах "Для кого самокат", "Про аренду", "Хотите оформить заказ"
        ordering_scooter.filling_order_fields_1()

        # Проверка, что заказ оформлен успешно (отображается окно "Заказ оформлен" с текстом "Заказ оформлен")
        assert ordering_scooter.verify_successful_order_text()


    @allure.title('Тест успешного заказа самоката при нажатии кнопки "Заказать" внизу главной страницы')
    def test_successful_scooter_order_button_order_below(self, driver):

        ordering_scooter = OrderingScooter(driver)

        # Нажать кнопку "Заказать" внизу главной страницы
        ordering_scooter.click_button_order_below()

        # Заполнение полей для заказа на страницах "Для кого самокат", "Про аренду", "Хотите оформить заказ"
        ordering_scooter.filling_order_fields_2()

        # Проверка, что заказ оформлен успешно (отображается окно "Заказ оформлен" с текстом "Заказ оформлен")
        assert ordering_scooter.verify_successful_order_text()


    @allure.title('Тест успешного перехода на главную страницу при нажатии на логотип «Самоката»')
    def test_successful_go_to_main_page_via_logo_scooter(self, driver_order):
        ordering_scooter = OrderingScooter(driver_order)

        # Нажать на логотип "Самоката"
        ordering_scooter.click_logo_scooter()

        # Проверка, что адрес открывшейся страницы - главная страница
        assert ordering_scooter.verify_main_url()


    @allure.title('Тест успешного перехода на главную страницу Дзена при нажатии на логотип Яндекса')
    def test_successful_go_to_dzen_page_via_logo_yandex(self, driver_order):
        ordering_scooter = OrderingScooter(driver_order)

        # Нажать на логотип Яндекса
        ordering_scooter.click_logo_yandex()

        # Переключиться на новую вкладку
        ordering_scooter.switch_to_last_window()

        # Дождаться, пока в адресной строке появится адрес Дзен
        ordering_scooter.wait_url_contains_dzen()

        # Проверка, что адрес открывшейся страницы - главная страница Дзена
        assert ordering_scooter.verify_dzen_url()
