import allure
from selenium.webdriver.common.by import By

from base_page import BasePage


class LeadershipPage(BasePage):
    LABEL_CTO_NAME = (By.XPATH, "//div[contains(@class, 'team-grid__info--name')]/p[contains(., 'Leonard Livschitz')]")
    TEXT_CTO_BIO = (By.CSS_SELECTOR, ".team-grid__modal-content-bio p")

    @allure.step("Open CTO info card")
    def open_cto_card(self):
        cto_name = self.wait_for_visibility(self.LABEL_CTO_NAME)
        cto_name.click()

    @allure.step("Get text of CTO info card")
    def get_card_text(self):
        cto_bio = self.wait_for_visibility(self.TEXT_CTO_BIO)
        return cto_bio.text
