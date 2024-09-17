import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    ACCEPT_COOKIES_BUTTON = (By.ID, "onetrust-accept-btn-handler")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Close cookies consent")
    def close_cookies_consent(self):
        accept_cookies = self.wait_for_visibility(self.ACCEPT_COOKIES_BUTTON)
        self.wait_for_animation_end(accept_cookies)
        accept_cookies.click()
        self.wait_to_disappear(accept_cookies)

    def wait_for_existence(self, locator: tuple[str, str]):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_animation_end(self, element: WebElement):
        max_iteration = 5
        location = element.location
        time.sleep(0.2)
        while max_iteration != 0:
            new_location = element.location
            if location == new_location:
                break
            else:
                location = new_location
                time.sleep(0.2)

    def wait_for_visibility(self, locator:  tuple[str, str]):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_to_disappear(self, locator):
        return self.wait.until(EC.invisibility_of_element(locator))

    def get_next_sibling(self, element: WebElement):
        return element.find_element(By.XPATH, "./following-sibling::*")

    def get_page_title(self):
        return self.driver.title

    def click_left(self, element: WebElement):
        offset_x = -element.rect["width"] / 2 + 10
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(element, offset_x, 0).click().perform()
