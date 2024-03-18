import allure

from helpers import OftenUseName, CommonAction


@allure.parent_suite('Заголовок 1')
@allure.suite('Раздел заголовка 1')
class TestPageSearch:
    @allure.title('Заголовок теста')
    @allure.severity('trivial')
    def test_case(self):
        # Описание
        allure.dynamic.description_html(
            f'{CommonAction.author(OftenUseName.sema)}<br /><br />{CommonAction.last_editor(OftenUseName.sasha)}'
        )
        # Шаги
        with allure.step('Первый тестовый шаг'):
            with allure.step('Первый тестовый результат'):
                pass
            #allure.attach.file(source='pictures/test.png', attachment_type=allure.attachment_type.PNG, name='Тестовая картинка')
        with allure.step('Второй тестовый шаг'):
            with allure.step('Второй тестовый результат'):
                pass