import allure
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.ordering_scooter_locators import (MainScooterLocators, OrderingScooterLocators, AboutRentLocators,
                                                OrderRegistrationLocators, OrderSuccessfullyPlacedLocators)
from helper.test_data import user_data_1, user_data_2, successful_message
from helper.url import main_url, dzen


main_scooter_locators = MainScooterLocators()
ordering_scooter_locators = OrderingScooterLocators()
about_rent_locators = AboutRentLocators()
order_registration_locators = OrderRegistrationLocators()
order_successfully_placed_locators = OrderSuccessfullyPlacedLocators()


class OrderingScooter(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажать кнопку "Заказать" вверху главной страницы')
    def click_button_order_on_top(self):

        # Подождать, пока кнопка "Заказать" станет кликабельна, нажать кнопку "Заказать
        self.wait_clickable_and_click(main_scooter_locators.button_order_on_top)



    @allure.step('Нажать кнопку "Заказать" внизу главной страницы')
    def click_button_order_below(self):

        #  Перейти к кнопке "Заказать" внизу (с использованием прокрутки)
        button_below = main_scooter_locators.button_order_below
        self.scroll(button_below)

        # Подождать, пока кнопка "Заказать" станет кликабельна, нажать кнопку "Заказать"
        self.wait_clickable_and_click(button_below)



    @allure.step('Заполнение полей для заказа на странице "Для кого самокат"')
    def filling_order_fields_who_is_scooter_for(self, user_data):

        # Подождать, пока кнопка "Далее" станет кликабельна
        button_next_view = ordering_scooter_locators.button_next
        self.wait_clickable(button_next_view)

        # Заполнить форму заказа
        # Заполнить поле "Имя"
        self.send_keys(ordering_scooter_locators.first_name_order, user_data.first_name)

        # Заполнить поле "Фамилия"
        self.send_keys(ordering_scooter_locators.last_name_order, user_data.last_name)

        # Заполнить поле "Адрес"
        self.send_keys(ordering_scooter_locators.address_order, user_data.address)

        # Нажать на поле "Станция метро"
        self.click(ordering_scooter_locators.metro_station_order)

        # Выбрать станцию метро
        self.wait_clickable_and_click(user_data.metro_station_locator)

        # Заполнить поле "Телефон"
        self.send_keys(ordering_scooter_locators.phone_order, user_data.phone)

        # Нажать кнопку "Далее"
        self.click(button_next_view)


    @allure.step('Заполнение полей для заказа на странице "Про аренду"')
    def filling_order_fields_about_rent(self, user_data):

        # Подождать, пока кнопка "Заказать" станет кликабельна
        button_order_view = about_rent_locators.button_rent_order
        self.wait_clickable(button_order_view)

        # Заполнить форму "Для кого самокат"
        # Заполнить поле "Когда привезти самокат"
        calendar = about_rent_locators.when_to_deliver_order
        self.wait_clickable_and_click(calendar)
        self.send_keys(calendar, user_data.when_to_deliver)
        self.send_keys(calendar, Keys.ENTER)

        # Заполнить поле "Срок аренды"
        self.wait_clickable_and_click(about_rent_locators.rental_period_order)
        self.wait_clickable_and_click(user_data.rental_period_locator)

        # Заполнить поле "Цвет самоката"
        self.click(user_data.color_scooter_locator)

        # Заполнить поле "Комментарий для курьера"
        self.send_keys(about_rent_locators.comment_order, user_data.comment)

        # Нажать кнопку "Заказать"
        self.click(button_order_view)


    @allure.step ('[Проверка, что заказ оформлен успешно (отображается окно "Заказ оформлен")')
    def verify_successful_order_text(self):
        return successful_message in self.get_text_when_visible(order_successfully_placed_locators.order_successfully_placed)


    @allure.step('Выбор варианта "Да" на странице "Хотите оформить заказ"')
    def select_yes_while_place_an_order(self):

        # Кликнуть вариант "Да" на странице "Хотите оформить заказ"
        self.wait_clickable_and_click(order_registration_locators.button_yes_order)


    @allure.step('Нажать на логотип "Самоката"')
    def click_logo_scooter(self):
        self.click(ordering_scooter_locators.scooter_logo_order)


    @allure.step('Нажать на логотип Яндекса')
    def click_logo_yandex(self):
        self.wait_clickable_and_click(main_scooter_locators.yandex_logo_order)


    @allure.step('Выбор объекта 1 с данными для заполнения полей заказа самоката')
    def filling_order_fields_1(self):
        self.filling_order_fields(user_data_1)


    @allure.step('Выбор объекта 2 с данными для заполнения полей заказа самоката')
    def filling_order_fields_2(self):
        self.filling_order_fields(user_data_2)


    @allure.step('Шаг по заполнению полей на страницах "Для кого самокат", "Про аренду", "Хотите оформить заказ"')
    def filling_order_fields(self, user_data):
        self.filling_order_fields_who_is_scooter_for(user_data)
        self.filling_order_fields_about_rent(user_data)
        self.select_yes_while_place_an_order()


    @allure.step('Дождаться, пока в адресной строке появится адрес Дзена')
    def wait_url_contains_dzen(self):
        return self.wait_url_contains(dzen)


    @allure.step('Проверка, что адрес открывшейся страницы - главная страница')
    def verify_main_url(self):
        return self.current_url() == main_url


    @allure.step('Проверка, что адрес открывшейся страницы - главная страница Дзена')
    def verify_dzen_url(self):
        return self.current_url() == dzen
