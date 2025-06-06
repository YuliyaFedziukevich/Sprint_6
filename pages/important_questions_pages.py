import allure
from pages.base_page import BasePage
from locators.important_questions_locators import ImportantQuestionLocators
from helper.answers_text import Text

important_question_locators = ImportantQuestionLocators()

class ImportantQuestionPages(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка соответствия ответов вопросам')
    def check_matching_answer_to_questions(self, index):

        question = important_question_locators.question_locators[index]
        answer = important_question_locators.answer_locators[index]

        # Перейти к вопросу (с использованием прокрутки)
        self.scroll(question)

        self.wait_clickable(question)

        # Получить текст вопроса, на которые предстоит кликнуть
        question_text_current = self.text(question)

        # Кликнуть на стрелочку с вопросом
        self.click(question)

        # Получить текст ответа, соответствующего вопросу
        answer_text_current = self.text(answer)

        # Проверка соответствия ответов вопросам:
        # - текст выбранного вопроса соответствует заданному требованиями,
        # - текст ответа выбранного вопроса соответствует заданному требованиями ответу
        assert question_text_current == Text.questions_text[index]
        assert answer_text_current == Text.answers_text[index]


