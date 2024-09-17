import pytest
import datetime

from ui.utils.driver import Driver


@pytest.fixture(scope="function")
def setup(request):
    driver = Driver.get_driver()
    driver.get("https://blog.griddynamics.com")
    yield driver
    if request.node.rep_call.failed:
        dt = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = "{}_{}".format(request.node.nodeid.replace("::", "_"), dt)
        with open(test_name + ".html", 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        driver.save_screenshot(test_name + ".png")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
