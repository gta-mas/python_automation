import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver = None

#@pytest.fixture(scope="class")
#def setup():
 #   print("First execution")
  #  yield
   # print("Last execution")


@pytest.fixture()
def load_data():
    print("User data being created")
    return ["Joe", "Doe", "website.com"]


@pytest.fixture(params=[("Chrome", "Joe", "Doe", "website"), ("Firefox", "Joe", "website"), ("Joe", "Doe", "IE")])
def cross_browser(request):
    return request.param

#command line hook to select specific browser/default to a specific browser
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome"
#     )
#=======================================================================================
#commands to setup a command line options for browser selection:
#browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         chrome_options = Options()
#         chrome_options.add_argument("--disable-exit-after-done")
#         chrome_options.add_argument("--start-maximized")
#
#         service_obj = Service("D:/Software Tester/chromedriver.exe")
#         driver = webdriver.Chrome(service=service_obj, options=chrome_options)
#         driver.implicitly_wait(5)
#
#     elif browser_name == "firefox":
#         #firefox invocation
#     elif browser_name == "IE":
#         #IE invocation
#
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     driver.maximize_window()
#======================================================================================


@pytest.fixture(scope="class")
def setup(request):
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--disable-exit-after-done")
    chrome_options.add_argument("--start-maximized")

    service_obj = Service("D:/Software Testing/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)



