import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.important_questions_locators import ImportantQuestionLocators
from helper.answers_text import Text

important_question_locators = ImportantQuestionLocators()

class ImportantQuestionPages:

    @allure.step('Проверка соответствия ответов вопросам')
    def check_matching_answer_to_questions(self, driver, index):

        # Перейти к вопросу (с использованием прокрутки)
        element = driver.find_element(*important_question_locators.question_locators[index])
        driver.execute_script('arguments[0].scrollIntoView();', element)


        wait = WebDriverWait(driver, 3)
        arrow = wait.until(expected_conditions.element_to_be_clickable(element))

        # Получить текст вопроса, на которые предстоит кликнуть
        question_text_current = arrow.text

        # Кликнуть на стрелочку с вопросом
        arrow.click()

        # Получить текст ответа, соответствующего вопросу
        answer_text_current = driver.find_element(*important_question_locators.answer_locators[index]).text

        # Проверка соответствия ответов вопросам:
        # - текст выбранного вопроса соответствует заданному требованиями,
        # - текст ответа выбранного вопроса соответствует заданному требованиями ответу
        assert question_text_current == Text.questions_text[index]
        assert answer_text_current == Text.answers_text[index]




