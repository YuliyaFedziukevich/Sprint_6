import allure
import pytest
from selenium import webdriver
from locators.important_questions_locators import ImportantQuestionLocators
from pages.important_questions_pages import ImportantQuestionPages
from helper.url import main_url

important_question_locators = ImportantQuestionLocators()
important_question_pages = ImportantQuestionPages()

class TestsImportantQuestions:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        # Перейти на сайт
        cls.driver.get(main_url)

    @allure.title('Тест на проверку соответствия полученного текста ответов соответствующим вопросам')
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_answers_correspond_to_question(self, index):
        important_question_pages.check_matching_answer_to_questions(self.driver, index)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

