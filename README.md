## Python for QA course capstone project

### API part
Contains tests for [Book service](https://github.com/griddynamics/PYTHON-QA-book-service)

### UI part
Contains tests for [Grid Dynamics blog](https://blog.griddynamics.com)

### How to run
1. Create venv `python3 -m venv <envname>`
2. Install dependencies `pip install -r requirements.txt` from **project root**
3. Navigate to project root directory
4. Run tests from **project root** like:
   * API - `PYTHONPATH=. pytest api/tests/tests_book.py --alluredir allure-results`
   * UI - `PYTHONPATH=. pytest ui/tests/tests_blog.py --alluredir allure-results`
5. To view report run `allure serve allure-results`

### Hints
* You can use `debug=true` env variable to get more detailed output