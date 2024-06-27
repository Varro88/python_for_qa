import requests
from requests import Response


class ApiClient:
    BASE_URL = "http://127.0.0.1:5000"

    def create_book(self, type, title, creation_date) -> Response:
        return requests.post(f"{self.BASE_URL}/v1/books/manipulation", json={
            "type": type,
            "title": title,
            "creation_date": creation_date
        })

    def get_book(self, book_id) -> Response:
        return requests.get(f"{self.BASE_URL}/v1/books/info?id={book_id}")

    def delete_book(self, book_id) -> Response:
        return requests.delete(f"{self.BASE_URL}/v1/books/manipulation?id={book_id}")