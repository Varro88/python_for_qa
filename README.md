## Python for QA capstone project

### API part
Contains tests for [Book service](https://github.com/griddynamics/PYTHON-QA-book-service)

### UI part
Contains tests for [Grid Dynamics blog](https://blog.griddynamics.com)

### How to run
1. Create venv
2. Install dependencies
3. Run like ` PYTHONPATH=. pytest api/tests/tests_book.py --alluredir allure-results` from **project root**
4. To view report run `allure serve allure-results`

### Hints
* You can use `debug=true` env variable to get more detailed output