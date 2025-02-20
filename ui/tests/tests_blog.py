import allure

from ui.pages.contacts_page import ContactsPage
from ui.pages.leadership_page import LeadershipPage
from ui.pages.main_page import MainPage


@allure.parent_suite("UI tests")
@allure.suite("Blog UI tests")
@allure.sub_suite("Main features of blog")
class TestsBlog:

    @allure.title("CTO personal info available on Leadership page")
    def test_cto_info(self, setup):
        """
        Case #1:
        1. Open https://blog.griddynamics.com
        2. Go to “Leadership” under About page
        3. Find Leonard Livschitz and click on the name
        4. Verify that information about Leonard has appeared. The text
        “director of Grid Dynamics’ board of directors since 2006 and the Chief Executive Officer of Grid Dynamics since 2014”
        is visible.
        """
        main_page = MainPage(setup)
        main_page.close_cookies_consent()
        main_page.open_leadership()
        leadership_page = LeadershipPage(setup)
        leadership_page.open_cto_card()
        actual_bio = leadership_page.get_card_text()
        expected_text = ("director of Grid Dynamics’ board of directors since 2006 "
                         "and the Chief Executive Officer of Grid Dynamics since 2014")
        assert expected_text in actual_bio

    @allure.title("Cloud and Devops topic filter updates the article list")
    def test_filters(self, setup):
        """
        Case #2:
        1. Open https://blog.griddynamics.com
        2. Click ‘filter’ (check it’s visible and available)
        3. Filter by Cloud and DevOps topic
        4. Check there is more than 1 article
        5. Reset all filters
        6. Check the first article in the list is different than in step 4 and check there is more than 1 article.
        """
        main_page = MainPage(setup)
        main_page.close_cookies_consent()
        main_page.apply_filter("Cloud and DevOps")
        cloud_devops_posts = main_page.get_posts_titles()
        assert len(cloud_devops_posts) > 1
        cloud_devops_first_posts = cloud_devops_posts[0].text
        main_page.apply_filter("All topics")
        all_posts = main_page.get_posts_titles()
        assert len(all_posts) > 1
        assert all_posts[0].text != cloud_devops_first_posts

    @allure.title("Contact form cannot be submitted without mandatory fields filled")
    def test_contacts(self, setup):
        """
        Case #3:
        1. Open https://blog.griddynamics.com
        2. Click on Get In Touch button
        3. Ensure page Contact Us opened
        4. Fill in the following:
          - First Name = Anna, Last Name = Smith
          - email = annasmith@griddynamics.com
          - select  What are you interested in? = Media inquiry
        5. Click on checkbox “I have read and accepted the Terms & Conditions and Privacy Policy”
        6. Click on checkbox “Subscribe to our latest insights & events”
        7. Ensure Contact button is inactive
        """
        main_page = MainPage(setup)
        main_page.close_cookies_consent()
        main_page.open_contacts()
        contacts_page = ContactsPage(setup)
        assert "contact us" in contacts_page.get_page_title().lower()
        contacts_page.set_firstname("Anna")
        contacts_page.set_lastname("Smith")
        contacts_page.set_email("annasmith@griddynamics.com")
        contacts_page.what_interested_in("Media inquiry")
        contacts_page.accept_terms()
        contacts_page.accept_subscribe()
        assert contacts_page.is_submit_disabled() is True
