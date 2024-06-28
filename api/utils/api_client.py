import logging

import requests
from requests import Response
from http.client import HTTPConnection
import os


class ApiClient:
    BASE_URL = "http://127.0.0.1:5000"

    if "debug" in os.environ and "true" == os.environ["debug"].lower():
        log = logging.getLogger('urllib3')
        log.setLevel(logging.DEBUG)
        HTTPConnection.debuglevel = 1

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
