import json
import pytest
from api.utils.api_client import ApiClient
import logging

logger = logging.getLogger()
file_content = open('api/resources/test_data.json')
test_data = json.load(file_content)


@pytest.fixture()
def existing_book():
    existing_book = test_data["existing_book"]
    api_client = ApiClient()
    response = api_client.create_book(existing_book["type"], existing_book["title"], existing_book["creation_date"])
    if response.status_code == 200:
        existing_book["id"] = response.json()["id"]
    else:
        logger.warning("Failed to create test data")
    return existing_book


@pytest.fixture()
def book_to_delete():
    book = test_data["book_to_delete"]
    api_client = ApiClient()
    response = api_client.create_book(book["type"], book["title"], book["creation_date"])
    if response.status_code == 200:
        book["id"] = response.json()["id"]
    else:
        logger.warning("Failed to create test data")
    return book
