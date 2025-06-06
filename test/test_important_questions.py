import allure
import pytest
from pages.important_questions_pages import ImportantQuestionPages

class TestsImportantQuestions:

    @allure.title('Тест на проверку соответствия полученного текста ответов соответствующим вопросам')
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_answers_correspond_to_question(self, driver, index):

        important_question_pages = ImportantQuestionPages(driver)
        important_question_pages.check_matching_answer_to_questions(index)






