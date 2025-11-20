from selene import have, command

from demoqa_tests import resource


class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser
        self.first_name = self.browser.element('#firstName')
        self.last_name = self.browser.element('#lastName')
        self.state = self.browser.element('#state')
        self.email = self.browser.element('#userEmail')
        self.gender = self.browser.all('[name=gender]')
        self.phone = self.browser.element('#userNumber')
        self.subjects = self.browser.element('#subjectsInput')
        self.hobbies = self.browser.all('.custom-checkbox')
        self.picture = self.browser.element('#uploadPicture')
        self.address = self.browser.element('#currentAddress')
        self.city = self.browser.element('#city')
        self.submit_button = self.browser.element('#submit')

    def open(self):
        self.browser.open('/automation-practice-form')
        self.browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        self.browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, first_name):
        self.first_name.type(first_name)
        return self

    def fill_last_name(self, last_name):
        self.last_name.type(last_name)
        return self

    def fill_email(self, email):
        self.email.type(email)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__month-select').type(month)
        self.browser.element('.react-datepicker__year-select').type(year)
        self.browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        self.browser.all('[id^=react-select][id*=option]').element_by(
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
        self.browser.element('#currentAddress').type(address)
        return self

    def fill_city(self, city):
        self.city.click()
        self.browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()


        return self

    def submit_form(self):
        self.submit_button.click().perform(command.js.click)
        return self

    def should_registered_user_with(self, full_name, email, male, phone, date_of_birth, subjects, hobbies, photo,
                                    address, state_city):
        self.browser.element('.table').all('td').even.should(
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
