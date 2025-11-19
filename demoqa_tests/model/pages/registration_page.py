from selene import have, command
from selene.support.conditions.have import value
from selene.support.shared import browser

from demoqa_tests import resource


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.state = browser.element('#state')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.phone = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('.custom-checkbox')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_gender(self, gender):
        self.gender.element_by(have.value(gender)).element('..').click()
        return self

    def fill_phone(self, phone):
        self.phone.type(phone)
        return self

    def fill_subjects(self, *subjects):
        for subject in subjects:
            self.subjects.type(subject).press_enter()

        return self

    def fill_hobbies(self, *hobbies):
        for hobby in hobbies:
            self.hobbies.element_by(have.exact_text(hobby)).click()
        return self

    def upload_picture(self):
        self.picture.set_value(resource.path('foto.jpg'))
        return self

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def fill_city(self, city):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()


        return self

    def submit_form(self):
        self.submit_button.click().perform(command.js.click)
        return self

    def should_registered_user_with(self, full_name, email, male, phone, date_of_birth, subjects, hobbies, photo,
                                    address, state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                male,
                phone,
                date_of_birth,
                subjects,
                hobbies,
                photo,
                address,
                state_city,
            )
        )
        return self
