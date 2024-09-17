import allure
from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class ContactsPage(BasePage):
    INPUT_FIRST_NAME = (By.ID, "get-in-touch-form-first_name")
    INPUT_LAST_NAME = (By.ID, "get-in-touch-form-last_name")
    INPUT_EMAIl = (By.ID, "get-in-touch-form-email")
    DROPDOWN_INTERESTED_IN = (By.CSS_SELECTOR, "div.get-in-touch-form__dropdown")
    LOCATOR_INTERESTED_IN_ITEM = "//div[@class='get-in-touch-form__dropdown-item' and text()='{}']"
    CHECKBOX_TERMS = (By.CSS_SELECTOR, "input[name='terms'] + span")
    CHECKBOX_SUBSCRIBE = (By.CSS_SELECTOR, "input[name='subscribe[]'] + span")

    BUTTON_SUBMIT = (By.CSS_SELECTOR, "div.get-in-touch-form__field > input[type='submit']")

    @allure.step("Fill first name")
    def set_firstname(self, text):
        self.wait_for_visibility(self.INPUT_FIRST_NAME).send_keys(text)

    @allure.step("Fill last name")
    def set_lastname(self, text):
        self.wait_for_visibility(self.INPUT_LAST_NAME).send_keys(text)

    @allure.step("Fill email")
    def set_email(self, text):
        self.wait_for_visibility(self.INPUT_EMAIl).send_keys(text)

    @allure.step("Select what are you interested in as '{}'")
    def what_interested_in(self, item):
        self.wait_for_visibility(self.DROPDOWN_INTERESTED_IN).click()
        selected_item = (By.XPATH, self.LOCATOR_INTERESTED_IN_ITEM.format(item))
        self.wait_for_visibility(selected_item).click()

    @allure.step("Accept terms")
    def accept_terms(self):
        checkbox = self.wait_for_existence(self.CHECKBOX_TERMS)
        self.click_left(checkbox)

    @allure.step("Subscribe")
    def accept_subscribe(self):
        subscribe = self.wait_for_existence(self.CHECKBOX_SUBSCRIBE)
        self.click_left(subscribe)

    @allure.step("Check if form can be submitted")
    def is_submit_disabled(self):
        return self.wait_for_visibility(self.BUTTON_SUBMIT).get_attribute("disabled") == 'true'
