from demoqa_tests.model.pages.registration_page import RegistrationPage
import allure


def test_student_registration_form(setup_browser):
    with allure.step("Открываем страницу регистрации"):
        registration_page = RegistrationPage(browser=setup_browser)
        registration_page.open()

    with allure.step("Заполняем имя"):
        registration_page.fill_first_name('Olga').fill_last_name('YA')

    with allure.step("Заполняем фамилию:"):
        registration_page.fill_email('name@example.com')

    with allure.step("Заполняем гендер"):
        registration_page.fill_gender('Female')

    with allure.step("Заполняем номер телефона"):
        registration_page.fill_phone('1234567891')

    with allure.step("Заполняем дату рождения"):
        registration_page.fill_date_of_birth('1999', 'May', '11')

    with allure.step("Заполняем сферу деятельности"):
        registration_page.fill_subjects('Computer Science', 'Accounting')

    with allure.step("Заполняем чекбокс хобби"):
        registration_page.fill_hobbies('Sports', 'Music')

    with allure.step("Загружаем фото"):
        registration_page.upload_picture()

    with allure.step("Заполняем адрес"):
        registration_page.fill_address('Moscowskaya Street 18')

    with allure.step("Выбираем страну"):
        registration_page.fill_state('NCR')

    with allure.step("Заполняем город"):
        registration_page.fill_city('Delhi')

    with allure.step("Отправляем форму"):
        registration_page.submit_form()

    with allure.step("Проверяем заполнение формы"):
        registration_page.should_registered_user_with(
            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science, Accounting',
            'Sports, Music',
            'foto.jpg',
            'Moscowskaya Street 18',
            'NCR Delhi',
        )
    '''
    # example of implementing assertion-free pageobjects
    registration_page.registered_user_data.should(
        have.exact_texts(
            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science',
            'Reading',
            'foto.jpg',
            'Moscowskaya Street 18',
            'NCR Delhi',
        )
    )
    '''
