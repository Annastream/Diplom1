import allure
from data import *

@allure.feature('Авторизация пользователя')
@allure.story('Тестирование различных сценариев авторизации')
class TestUserLogin:

    @allure.title('Тест успешного входа с корректными данными')
    def test_login_successful(self, login_user):
        with allure.step('Отправляем запрос на вход с существующими данными'):
            response = login_user(EXISTING_USER)

        with allure.step('Проверяем успешный ответ'):
            assert response.status_code == 200, \
                f"Ожидался код 200, получен {response.status_code}. Ответ: {response.text}"
            response_json = response.json()
            assert all(key in response_json for key in LOGIN_SUCCESS_RESPONSE.keys()), \
                f"В ответе отсутствуют ожидаемые ключи. Ответ: {response_json}"
            assert response_json["user"]["email"] == EXISTING_USER["email"], \
                "Email пользователя не совпадает"

    @allure.title('Тест неуспешного входа с неверными данными')
    def test_login_invalid_credentials(self, login_user):
        with allure.step('Отправляем запрос на вход с неверными данными'):
            response = login_user(INVALID_USER)

        with allure.step('Проверяем ошибку авторизации'):
            assert response.status_code == 401, \
                f"Ожидался код 401, получен {response.status_code}. Ответ: {response.text}"
            assert response.json() == INVALID_CREDENTIALS_RESPONSE, \
                f"Ожидался ответ {INVALID_CREDENTIALS_RESPONSE}, получен: {response.json()}"