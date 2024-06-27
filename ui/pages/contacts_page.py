import allure
from selenium.webdriver.common.by import By

from base_page import BasePage


class ContactsPage(BasePage):
    INPUT_FIRST_NAME = (By.ID, "get-in-touch-form-first_name")
    INPUT_LAST_NAME = (By.ID, "get-in-touch-form-last_name")
    INPUT_EMAIl = (By.ID, "get-in-touch-form-email")
    INPUT_HOW_DID_HEAR = (By.CSS_SELECTOR, "div.get-in-touch-form__dropdown")
    LOCATOR_DROPDOWN_ITEM = "//div[contains(@class, 'get-in-touch-form__dropdown--item') and .='{}']"

    CHECKBOX_TERMS = (By.NAME, "terms[]")
    CHECKBOX_CONTACT_ME = (By.NAME, "contact_back[]")

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

    @allure.step("Select how did you hear about us as '{}'")
    def set_how_did_hear(self, text):
        self.wait_for_visibility(self.INPUT_HOW_DID_HEAR).click()
        selected_item = (By.XPATH, self.LOCATOR_DROPDOWN_ITEM.format(text))
        self.wait_for_visibility(selected_item).click()

    @allure.step("Accept terms")
    def accept_terms(self):
        terms = self.wait_for_existence(self.CHECKBOX_TERMS)
        checkbox = self.get_next_sibling(terms)
        self.click_left(checkbox)

    @allure.step("Allow to contact")
    def accept_contact_me(self):
        contact_me = self.wait_for_existence(self.CHECKBOX_CONTACT_ME)
        self.get_next_sibling(contact_me).click()

    def is_submit_enabled(self):
        return self.wait_for_visibility(self.BUTTON_SUBMIT).get_attribute("disabled") == 'true'
