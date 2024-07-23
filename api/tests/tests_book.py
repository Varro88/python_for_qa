import allure
import pytest
from hamcrest import assert_that, equal_to, matches_regexp, less_than
from api.utils import helper
from api.utils.api_client import ApiClient
from faker import Faker


@allure.parent_suite("API tests")
@allure.suite("Book API tests")
@allure.sub_suite("Main features of Book API")
class TestsBook:
    # Note: in description wrong type is mentioned: supported one is "Adventure", NOT "Action and Adventure"
    UUID_REGEXP = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    faker = Faker()

    @allure.title("Create the book passes")
    def test_create_book(self):
        type = helper.get_random_type()
        title = self.faker.text(20)
        creation_date = self.faker.date()
        response = ApiClient().create_book(type, title, creation_date)
        assert_that(response.status_code, equal_to(200))
        body = response.json()
        assert_that(body["type"], equal_to(type))
        assert_that(body["title"], equal_to(title))
        assert_that(body["creation_date"], equal_to(creation_date))
        assert_that(body["type"], equal_to(type))
        assert_that(body["id"], matches_regexp(self.UUID_REGEXP))
        seconds_diff = helper.get_seconds_diff(body["updated_date_time"])
        assert_that(seconds_diff, less_than(1))

    @allure.title("Create the book with  '{type}' as type")
    @pytest.mark.parametrize("type", ["Science", "Satire", "Drama", "Adventure", "Romance"])
    def test_valid_book_types(self, type):
        title = self.faker.text(20)
        creation_date = self.faker.date()
        response = ApiClient().create_book(type, title, creation_date)
        assert_that(response.status_code, equal_to(200))
        body = response.json()
        assert_that(body["type"], equal_to(type))
        assert_that(body["title"], equal_to(title))
        assert_that(body["creation_date"], equal_to(creation_date))
        assert_that(body["type"], equal_to(type))
        assert_that(body["id"], matches_regexp(self.UUID_REGEXP))
        seconds_diff = helper.get_seconds_diff(body["updated_date_time"])
        assert_that(seconds_diff, less_than(1))

    @allure.title("Create the book with empty title passes")
    def test_create_book_empty_title(self):
        type = helper.get_random_type()
        title = ""
        creation_date = self.faker.date()
        response = ApiClient().create_book(type, title, creation_date)
        assert_that(response.status_code, equal_to(200))
        body = response.json()
        assert_that(body["type"], equal_to(type))
        assert_that(body["title"], equal_to(title))
        assert_that(body["creation_date"], equal_to(creation_date))
        assert_that(body["type"], equal_to(type))
        assert_that(body["id"], matches_regexp(self.UUID_REGEXP))
        seconds_diff = helper.get_seconds_diff(body["updated_date_time"])
        assert_that(seconds_diff, less_than(1))

    @allure.title("Create the book with null date passes")
    def test_create_book_null_date(self):
        type = helper.get_random_type()
        title = self.faker.text(20)
        creation_date = None
        response = ApiClient().create_book(type, title, creation_date)
        assert_that(response.status_code, equal_to(200))
        body = response.json()
        assert_that(body["type"], equal_to(type))
        assert_that(body["title"], equal_to(title))
        assert_that(body["creation_date"], equal_to(creation_date))
        assert_that(body["type"], equal_to(type))
        assert_that(body["id"], matches_regexp(self.UUID_REGEXP))
        seconds_diff = helper.get_seconds_diff(body["updated_date_time"])
        assert_that(seconds_diff, less_than(1))

    @allure.title("Create the book with null title returns error 400")
    def test_create_book_null_title(self):
        type = helper.get_random_type()
        title = None
        creation_date = self.faker.date()
        response = ApiClient().create_book(type, title, creation_date)
        assert_that(response.status_code, equal_to(400))
        assert_that(response.json()["message"], equal_to("The book entity is not valid."))

    @allure.title("Create the book with empty type returns error 400")
    def test_create_book_empty_type(self):
        type = ""
        title = self.faker.text(20)
        creation_date = self.faker.date()
        response = ApiClient().create_book(type, title, creation_date)
        assert_that(response.status_code, equal_to(400))
        assert_that(response.json()["message"], equal_to("The book entity is not valid."))

    @allure.title("Create the book with wrong date format returns error 400")
    def test_create_book_wrong_date(self):
        type = helper.get_random_type()
        title = self.faker.text(20)
        creation_date = "2021-30-02"
        response = ApiClient().create_book(type, title, creation_date)
        assert_that(response.status_code, equal_to(400))
        assert_that(response.json()["message"], equal_to("The book entity is not valid."))

    @allure.title("Get existing book")
    def test_get_existing_book(self, existing_book):
        response = ApiClient().get_book(existing_book["id"])
        assert_that(response.status_code, equal_to(200))
        body = response.json()
        assert_that(body["type"], equal_to(existing_book["type"]))
        assert_that(body["title"], equal_to(existing_book["title"]))
        assert_that(body["creation_date"], equal_to(existing_book["creation_date"]))
        assert_that(body["id"], matches_regexp(self.UUID_REGEXP))
        seconds_diff = helper.get_seconds_diff(body["updated_date_time"])
        assert_that(seconds_diff, less_than(1))

    @allure.title("Get not existing book")
    def test_get_not_existing_book(self):
        response = ApiClient().get_book("wrong-id")
        assert_that(response.status_code, equal_to(404))

    @allure.title("Delete book")
    def test_delete_existing_book(self, book_to_delete):
        delete_response = ApiClient().delete_book(book_to_delete["id"])
        assert_that(delete_response.status_code, equal_to(200))
        get_response = ApiClient().get_book(book_to_delete["id"])
        assert_that(get_response.status_code, equal_to(404))

    @allure.title("Delete not existing book")
    def test_delete_not_existing_book(self):
        delete_response = ApiClient().delete_book("wrong-id")
        assert_that(delete_response.status_code, equal_to(404))



