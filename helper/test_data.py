# Данныe для входа в аккаунт и для проверки сообщений

from locators.ordering_scooter_locators import AboutRentLocators, OrderingScooterLocators

about_rent_locators = AboutRentLocators()
ordering_scooter_locators = OrderingScooterLocators()


class UserData:
    def __init__(self, first_name, last_name, address, metro_station_locator, phone, when_to_deliver, rental_period_locator, color_scooter_locator, comment ):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.metro_station_locator = metro_station_locator
        self.phone = phone
        self.when_to_deliver = when_to_deliver
        self.rental_period_locator = rental_period_locator
        self.color_scooter_locator = color_scooter_locator
        self.comment = comment

user_data_1 = UserData(
    first_name='Иван',
    last_name='Иванов',
    address='г. Москва, ул. Советская, д. 1, кв. 1',
    metro_station_locator = ordering_scooter_locators.metro_station_komsomolskaya_order,
    phone='+1111222333',
    when_to_deliver='11.11.2025',
    rental_period_locator = about_rent_locators.rental_period_2_days_order,
    color_scooter_locator = about_rent_locators.black_color_scooter_order,
    comment='Доставка желательна с утра')

user_data_2 = UserData(
    first_name = 'Петр',
    last_name = 'Петров',
    address = 'г. Москва, ул. Ленина, д. 2, кв. 2',
    metro_station_locator = ordering_scooter_locators.metro_station_sokolniki_order,
    phone = '+1444555666',
    when_to_deliver = '12.12.2025',
    rental_period_locator = about_rent_locators.rental_period_3_days_order,
    color_scooter_locator = about_rent_locators.grey_color_scooter_order,
    comment = 'Доставка желательна вечером')

# Текст сообщения об успешном заказе самоката
successful_message = 'Заказ оформлен'