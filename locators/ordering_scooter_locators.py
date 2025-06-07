from selenium.webdriver.common.by import By

# Локаторы для заказа самоката на главной странице
class MainScooterLocators:

    # Кнопка "Заказать" внизу страницы
    button_order_below = (By.XPATH, '//div[contains(@class, "Home_FinishButton__1")]/button[text()="Заказать"]')

    # Кнопка "Заказать" вверху страницы
    button_order_on_top = (By.XPATH, '//div[contains(@class, "Header_Nav__AGCXC")]/button[text()="Заказать"]')

    # логотип «Яндекс»
    yandex_logo_order = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]')

    pop_up_window_exit = (By.XPATH, '//span[@aria-label = "Закрыть"]')


# Локаторы для заказа самоката на странице "Для кого самокат"
class OrderingScooterLocators:

    # Поле для ввода имени на странице "Для кого самокат"
    first_name_order = (By.XPATH, '//input[@placeholder ="* Имя"]')

    # Поле для ввода фамилии на странице "Для кого самокат"
    last_name_order = (By.XPATH, '//input[@placeholder ="* Фамилия"]')

    # Поле для ввода адреса на странице "Для кого самокат"
    address_order = (By.XPATH, '//input[@placeholder ="* Адрес: куда привезти заказ"]')

    # Поле для ввода станции метро на странице "Для кого самокат"
    metro_station_order = (By.XPATH, '//input[@placeholder ="* Станция метро"]')

    # Cтанция метро "Комсомольская" на странице "Для кого самокат"
    metro_station_komsomolskaya_order = (By.XPATH, '//li[@class = "select-search__row"]//div[text() = "Комсомольская"]')

    # Cтанция метро "Сокольники" на странице "Для кого самокат"
    metro_station_sokolniki_order = (By.XPATH, '//li[@class = "select-search__row"]//div[text() = "Сокольники"]')

    # Поле для ввода телефона на странице "Для кого самокат"
    phone_order = (By.XPATH, '//input[@placeholder ="* Телефон: на него позвонит курьер"]')

    # Кнопка "Далее" на странице "Для кого самокат"
    button_next = (By.XPATH, '//button[text() = "Далее"]')

    # логотип «Самоката»
    scooter_logo_order = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')


# Локаторы для заказа скутера на странице "Про аренду"
class AboutRentLocators:

    # Поле для ввода даты доставки самоката на странице "Про аренду"
    when_to_deliver_order = (By.XPATH, '//input[@placeholder ="* Когда привезти самокат"]')

    # Поле для выбора срока аренды на странице "Про аренду"
    rental_period_order = (By.XPATH, '//div[text() = "* Срок аренды"]')

    # Поле для выбора срока аренды "двое суток" на странице "Про аренду"
    rental_period_2_days_order =(By.XPATH, '//div[text() = "двое суток"]')

    # Поле для выбора срока аренды "трое суток" на странице "Про аренду"
    rental_period_3_days_order = (By.XPATH, '//div[text() = "трое суток"]')

    # Поле для выбора черного цвета самоката на странице "Про аренду"
    black_color_scooter_order = (By.ID, 'black')

    # Поле для выбора цвета самоката "серая безысходность" на странице "Про аренду"
    grey_color_scooter_order = (By.ID, 'grey')

    # Поле для ввода комментария на странице "Про аренду"
    comment_order = (By.XPATH, '//input[@placeholder ="Комментарий для курьера"]')

    # Кнопка "Заказать" на странице "Про аренду"
    button_rent_order = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')


# Локаторы для страницы "Хотите оформить заказ"
class OrderRegistrationLocators:

    # Кнопка "Да" на странице "Хотите оформить заказ"
    button_yes_order = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Да"]')


# Локатор для страницы "Заказ оформлен"
class OrderSuccessfullyPlacedLocators:
    # Окно "Заказ оформлен"
    order_successfully_placed = (By.XPATH, '//div[contains(@class, "Order_Modal")]/div[text() = "Заказ оформлен"]')






