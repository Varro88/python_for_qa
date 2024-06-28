import allure
from selenium.webdriver.common.by import By

from base_page import BasePage


class MainPage(BasePage):
    MENU_ITEM_ABOUT = (By.CSS_SELECTOR, "a[href='https://www.griddynamics.com/about']")
    MENU_ITEM_LEADERSHIP = (By.CSS_SELECTOR, "a[href='https://www.griddynamics.com/leadership']")
    BUTTON_GET_IN_TOUCH = (By.CSS_SELECTOR, "div.contact.menu-item>a[href='https://www.griddynamics.com/contact']>span.title")
    BUTTON_BURGER = (By.CSS_SELECTOR, "button.primary-menu__burger")

    LABEL_FILTER = (By.CSS_SELECTOR, ".blog-page__filter--title")
    DROPDOWN_TOPICS = (By.ID, "sub-category-list")
    DROPDOWN_ITEM_LOCATOR = "//span[contains(@class, 'sub-category-item') and contains(., '{}')]"
    TITLE_ACTIVE_TOPIC = (By.CSS_SELECTOR, "div.blog-page__category-name > a > h2")
    TITLE_SELECTED_TOPICS = (By.CSS_SELECTOR, ".blog-page__category-name>a>h2")
    BLOCK_ARTICLE = (By.CSS_SELECTOR, ".blog-page__post-item")
    TITLE_POSTS = (By.CSS_SELECTOR, "div.blog-page__category-item:not(.disabled) a.blog-page__post-item h3")

    @allure.step("Open burger menu")
    def open_burger_menu(self):
        burger = self.driver.find_element(*self.BUTTON_BURGER)
        burger.click()

    @allure.step("Open get in touch form")
    def open_contacts(self):
        self.open_burger_menu()
        get_in_touch_button = self.wait_for_visibility(self.BUTTON_GET_IN_TOUCH)
        get_in_touch_button.click()

    @allure.step("Open Leadership page")
    def open_leadership(self):
        self.open_burger_menu()
        about = self.wait_for_visibility(self.MENU_ITEM_ABOUT)
        about.click()
        leadership = self.wait_for_visibility(self.MENU_ITEM_LEADERSHIP)
        leadership.click()

    @allure.step("Apply filter by '{1}' topic")
    def apply_filter(self, topic):
        topics_dropdown = self.wait_for_visibility(self.DROPDOWN_TOPICS)
        topics_dropdown.click()
        topic_tuple = (By.XPATH, self.DROPDOWN_ITEM_LOCATOR.format(topic))
        item_to_select = self.wait_for_visibility(topic_tuple)
        item_to_select.click()

    @allure.step("Get post titles")
    def get_posts_titles(self):
        return self.driver.find_elements(*self.TITLE_POSTS)
