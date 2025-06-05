from selenium.webdriver.common.by import By


class ImportantQuestionLocators:

    # Вопрос 1. "Сколько это стоит? И как оплатить?"
    question_1_locator = (By.ID, 'accordion__heading-0')

    # Вопрос 2. "Хочу сразу несколько самокатов! Так можно?"
    question_2_locator = (By.ID, 'accordion__heading-1')

    # Вопрос 3. "Как рассчитывается время аренды?"
    question_3_locator = (By.ID, 'accordion__heading-2')

    # Вопрос 4. "Можно ли заказать самокат прямо на сегодня?"
    question_4_locator = (By.ID, 'accordion__heading-3')

    # Вопрос 5. "Можно ли продлить заказ или вернуть самокат раньше?"
    question_5_locator = (By.ID, 'accordion__heading-4')

    # Вопрос 6. "Вы привозите зарядку вместе с самокатом?"
    question_6_locator = (By.ID, 'accordion__heading-5')

    # Вопрос 7. "Можно ли отменить заказ?"
    question_7_locator = (By.ID, 'accordion__heading-6')

    # Вопрос 8. "Я жизу за МКАДом, привезёте?"
    question_8_locator = (By.ID, 'accordion__heading-7')

    # Список локаторов для вопросов
    question_locators =[question_1_locator, question_2_locator, question_3_locator, question_4_locator, question_5_locator,
                        question_6_locator, question_7_locator, question_8_locator]
    # Ответ  на вопрос 1.
    answer_1_locator = (By.ID, 'accordion__panel-0')

    # Ответ  на вопрос 2.
    answer_2_locator = (By.ID, 'accordion__panel-1')

    # Ответ  на вопрос 3.
    answer_3_locator = (By.ID, 'accordion__panel-2')

    # Ответ  на вопрос 4.
    answer_4_locator = (By.ID, 'accordion__panel-3')

    # Ответ  на вопрос 5.
    answer_5_locator = (By.ID, 'accordion__panel-4')

    # Ответ  на вопрос 6.
    answer_6_locator = (By.ID, 'accordion__panel-5')

    # Ответ  на вопрос 7.
    answer_7_locator = (By.ID, 'accordion__panel-6')

    # Ответ  на вопрос 8.
    answer_8_locator = (By.ID, 'accordion__panel-7')

    # Список локаторов для ответов
    answer_locators = [answer_1_locator, answer_2_locator, answer_3_locator, answer_4_locator,
                       answer_5_locator, answer_6_locator, answer_7_locator, answer_8_locator]

