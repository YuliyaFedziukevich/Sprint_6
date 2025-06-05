import allure
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.ordering_scooter_locators import (MainScooterLocators, OrderingScooterLocators, AboutRentLocators,
                                                OrderRegistrationLocators, OrderSuccessfullyPlacedLocators)
main_scooter_locators = MainScooterLocators()
ordering_scooter_locators = OrderingScooterLocators()
about_rent_locators = AboutRentLocators()
order_registration_locators = OrderRegistrationLocators()
order_successfully_placed_locators = OrderSuccessfullyPlacedLocators()


class OrderingScooter:

    @allure.step('Нажать кнопку "Заказать" вверху главной страницы')
    def click_button_order_on_top(self, driver):

        # Подождать, пока кнопка "Заказать" станет кликабельна
        wait = WebDriverWait(driver, 3)
        button_order = wait.until(expected_conditions.element_to_be_clickable(main_scooter_locators.button_order_on_top))

        # Нажать кнопку "Заказать
        button_order.click()


    @allure.step('Нажать кнопку "Заказать" внизу главной страницы')
    def click_button_order_below(self, driver):

        #  Перейти к кнопке "Заказать" внизу (с использованием прокрутки)
        element = driver.find_element(*main_scooter_locators.button_order_below)
        driver.execute_script('arguments[0].scrollIntoView();', element)

        # Подождать, пока кнопка "Заказать" станет кликабельна
        wait = WebDriverWait(driver, 10)
        # Нажать кнопку "Заказать"
        wait.until(expected_conditions.element_to_be_clickable(element)).click()


    @allure.step('Заполнение полей для заказа на странице "Для кого самокат"')
    def filling_order_fields_who_is_scooter_for(self, driver, user_data):

        # Подождать, пока кнопка "Далее" станет кликабельна
        wait = WebDriverWait(driver, 3)
        button_next_view = wait.until(expected_conditions.element_to_be_clickable(ordering_scooter_locators.button_next))

        # Заполнить форму заказа

        # Заполнить поле "Имя"
        driver.find_element(*ordering_scooter_locators.first_name_order).send_keys(user_data.first_name)

        # Заполнить поле "Фамилия"
        driver.find_element(*ordering_scooter_locators.last_name_order).send_keys(user_data.last_name)

        # Заполнить поле "Адрес"
        driver.find_element(*ordering_scooter_locators.address_order).send_keys(user_data.address)

        # Нажать на поле "Станция метро"
        driver.find_element(*ordering_scooter_locators.metro_station_order).click()

        # Выбрать станцию метро
        metro_option = wait.until(expected_conditions.element_to_be_clickable(user_data.metro_station_locator))
        metro_option.click()

        # Заполнить поле "Телефон"
        driver.find_element(*ordering_scooter_locators.phone_order).send_keys(user_data.phone)

        # Нажать кнопку "Далее"
        button_next_view.click()


    @allure.step('Заполнение полей для заказа на странице "Про аренду"')
    def filling_order_fields_about_rent(self, driver, user_data):

        # Подождать, пока кнопка "Заказать" станет кликабельна
        wait = WebDriverWait(driver, 3)
        button_next_view = wait.until(expected_conditions.element_to_be_clickable(about_rent_locators.button_rent_order))

        # Заполнить форму "Для кого самокат"

        # Заполнить поле "Когда привезти самокат"
        calendar = driver.find_element(*about_rent_locators.when_to_deliver_order)
        calendar.click()
        calendar.send_keys(user_data.when_to_deliver)
        calendar.send_keys(Keys.ENTER)

        # Заполнить поле "Срок аренды"
        driver.find_element(*about_rent_locators.rental_period_order).click()
        rent = wait.until(expected_conditions.element_to_be_clickable(user_data.rental_period_locator))
        rent.click()

        # Заполнить поле "Цвет самоката"
        driver.find_element(*user_data.color_scooter_locator).click()

        # Заполнить поле "Комментарий для курьера"
        driver.find_element(*about_rent_locators.comment_order).send_keys(user_data.comment)

        # Нажать кнопку "Заказать"
        button_next_view.click()


    @allure.step('Выбор варианта "Да" на странице "Хотите оформить заказ"')
    def select_yes_while_place_an_order(self, driver):

        # Кликнуть вариант "Да" на странице "Хотите оформить заказ"
        wait = WebDriverWait(driver, 3)
        button_yes = wait.until(expected_conditions.element_to_be_clickable(order_registration_locators.button_yes_order))
        button_yes.click()


    @allure.step('Шаг по заполнению полей на страницах "Для кого самокат", "Про аренду", "Хотите оформить заказ"')
    def filling_order_fields(self, driver, user_data):
        self.filling_order_fields_who_is_scooter_for(driver, user_data)
        self.filling_order_fields_about_rent(driver, user_data)
        self.select_yes_while_place_an_order(driver)

