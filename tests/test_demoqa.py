import os.path
from selene.support.shared import browser
from selene import be, have

def test_practice_form_submit(set_browser_resolution):
    #GIVEN
    browser.open('https://demoqa.com/automation-practice-form')

    #WHEN
    browser.element('#firstName').should(be.blank).type('Pavel')

    browser.element('#lastName').should(be.blank).type('Gorozhankin')

    browser.element('#userEmail').should(be.blank).type('test_mail@test.mail')

    browser.element('[value="Male"]~label').click()

    browser.element('#userNumber').should(be.blank).type('7900123456')

    browser.element('#dateOfBirthInput').should(be.not_.blank).click()
    browser.element('.react-datepicker__month-select>[value="4"]').click()
    browser.element('.react-datepicker__year-select>[value="1992"]').click()
    browser.element('[aria-label*="May 7th, 1992"]').click()

    browser.element('#subjectsInput').should(be.blank).type('math')
    browser.element('#react-select-2-option-0').click()

    browser.element('#hobbies-checkbox-3~label').click()

    avatar_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'avatar.jpg')
    browser.element('#uploadPicture').set_value(avatar_path)

    browser.element('#currentAddress').should(be.blank).type('Russia, Samara')

    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()

    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').click()

    #THEN
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive')\
        .should(have.text('Student Name Pavel Gorozhankin'))\
        .should(have.text('Student Email test_mail@test.mail'))\
        .should(have.text('Gender Male'))\
        .should(have.text('Mobile 7900123456'))\
        .should(have.text('Date of Birth 07 May,1992'))\
        .should(have.text('Subjects Maths'))\
        .should(have.text('Hobbies Music')) \
        .should(have.text('Picture avatar.jpg')) \
        .should(have.text('Address Russia, Samara'))\
        .should(have.text('State and City Uttar Pradesh Agra'))