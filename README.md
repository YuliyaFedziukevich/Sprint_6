* **Тестовые сценарии**:
* 1 Выпадающий список в разделе «Вопросы о важном»;
* 2 Заказ самоката. 

* **Перечень используемых папок и файлов для каждого из сценариев**:
* 1 Выпадающий список в разделе «Вопросы о важном»: 
* - helper/answers_text.py, helper/test_data.py, - helper/url,
* - locators/important_questions_locators.py, 
* - pages/base_page, pages/important_questions_pages.py, 
* - test_important_questions.py.
* 2 **Заказ самоката:
* - helper/test_data.py, helper/url,
* - locators/ordering_scooter_locators.py, 
* - pages/base_page, pages/ordering_scooter_pages.py, 
* - test/test_ordering_scooter.py.

* **Перечень папок и файлов**:
* 1 **helper** - содержит тестовые данные, используемые в обоих сценариях:
* - answers_text.py - содержит тексты вопросов и ответов в разделе «Вопросы о важном»;
* - test_data.py - содержит тестовые данные для оформления заказа самоката и текст сообщения об успешном заказе самоката;
* -  url - содержит используемые url
- 2 **locators** - содержит файлы с локаторами, используемыми в каждом из сценариев:
* - important_questions_locators.py - локаторы выпадающего списка в разделе «Вопросы о важном»;
* - ordering_scooter_locators.py - локаторы для окон заказа самоката
* 3 **pages** - содержит методы и шаги, используемые в каждом из сценариев:
* - base_page - общие методы для тестирования;
* - important_questions_pages.py - методы для тестирования выпадающего списка в разделе «Вопросы о важном»;
* - ordering_scooter_pages.py - методы для тестирования окон заказа самоката.
* 4 **results** - Allure-отчёт в формате JSON
* 5 **test** - содержит тесты для каждого из сценариев:
* - test_important_questions.py - тесты для выпадающего списка в разделе «Вопросы о важном»;
* - test/test_ordering_scooter.py - тесты заказа самоката;
* 6 conftest.py - содержит фикстуры; 
* 7 requirements.txt - файл с внешними зависимостями;
* 8 allure_report - сгенерированный Allure-отчёт
