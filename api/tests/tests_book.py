import allure
from api.utils.api_client import ApiClient
from faker import Faker


class TestsBook:

    # Note: in description wrong type is mentioned: supported one is "Adventure", NOT "Action and Adventure"
    valid_types = ["Science", "Satire", "Drama", "Adventure", "Romance"]
    faker = Faker()

    @allure.title("Create the book passes")
    def test_create_book(self):
        type = self.valid_types[self.faker.pyint(0, len(self.valid_types)-1)]
        title = self.faker.text(20)
        creation_date = self.faker.date()
        response = ApiClient().create_book(type, title, creation_date)
        assert response.status_code == 200
        body = response.json()
        assert body["type"] == type
        assert body["title"] == title
        assert body["creation_date"] == creation_date
        assert "id" in body
        assert "updated_date_time" in body

    @allure.title("Create the book with null date passes")
    def test_create_book_null_date(self):
        type = self.valid_types[self.faker.pyint(0, len(self.valid_types) - 1)]
        title = self.faker.text(20)
        creation_date = None
        response = ApiClient().create_book(type, title, creation_date)
        assert response.status_code == 200
        body = response.json()
        assert body["type"] == type
        assert body["title"] == title
        assert body["creation_date"] == creation_date
        assert "id" in body
        assert "updated_date_time" in body

    @allure.title("Create the book with empty title passes")
    def test_create_book_empty_title(self):
        type = self.valid_types[self.faker.pyint(0, len(self.valid_types) - 1)]
        title = ""
        creation_date = self.faker.date()
        response = ApiClient().create_book(type, title, creation_date)
        assert response.status_code == 200
        body = response.json()
        assert body["type"] == type
        assert body["title"] == title
        assert body["creation_date"] == creation_date
        assert "id" in body
        assert "updated_date_time" in body

    @allure.title("Create the book with null date passes")
    def test_create_book_null_title(self):
        type = self.valid_types[self.faker.pyint(0, len(self.valid_types) - 1)]
        title = self.faker.text(20)
        creation_date = None
        response = ApiClient().create_book(type, title, creation_date)
        assert response.status_code == 200
        body = response.json()
        assert body["type"] == type
        assert body["title"] == title
        assert body["creation_date"] is None
        assert "id" in body
        assert "updated_date_time" in body

    @allure.title("Create the book with empty type fails")
    def test_create_book_empty_type(self):
        type = ""
        title = self.faker.text(20)
        creation_date = self.faker.date()
        response = ApiClient().create_book(type, title, creation_date)
        assert response.status_code == 400
        assert response.json()["message"] == "The book entity is not valid."

    @allure.title("Create the book with wrong date format fails")
    def test_create_book_wrong_date(self):
        type = self.valid_types[self.faker.pyint(0, len(self.valid_types) - 1)]
        title = self.faker.text(20)
        creation_date = "2021-30-02"
        response = ApiClient().create_book(type, title, creation_date)
        assert response.status_code == 400
        assert (response.json()["message"] == "The book entity is not valid.")

    @allure.title("Get existing book")
    def test_get_existing_book(self, existing_book):
        response = ApiClient().get_book(existing_book["id"])
        assert response.status_code == 200
        body = response.json()
        assert body["type"] == existing_book["type"]
        assert body["title"] == existing_book["title"]
        assert body["creation_date"] == existing_book["creation_date"]
        assert body["id"] == existing_book["id"]

    @allure.title("Get not existing book")
    def test_get_not_existing_book(self):
        response = ApiClient().get_book("wrong-id")
        assert response.status_code == 404

    @allure.title("Delete book")
    def test_delete_existing_book(self, book_to_delete):
        delete_response = ApiClient().delete_book(book_to_delete["id"])
        assert delete_response.status_code == 200
        get_response = ApiClient().get_book(book_to_delete["id"])
        assert get_response.status_code == 404

    @allure.title("Delete not existing book")
    def test_delete_not_existing_book(self):
        delete_response = ApiClient().delete_book("wrong-id")
        assert delete_response.status_code == 404



