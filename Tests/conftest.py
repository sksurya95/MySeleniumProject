import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Config.Config import COUNTRY_VARIABLES

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_experimental_option("detach", True)


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="uat",
        help="Environment to run tests against: sit or uat"
    )
    parser.addoption(
        "--country",
        action="store",
        default=None,
        help="Country to run the test for"
    )


@pytest.fixture(scope="class")
def cp(request):
    env = request.config.getoption("--env")
    country = request.config.getoption("--country")

    if env == "sit":
        url = "https://vce--vcesit2.sandbox.my.site.com/customers/s/login/?language=en_US&ec=302&startURL=%2Fcustomers%2Fs%2F"
    elif env == "uat":
        url = "https://connect-uat.volvoce.com/customers/s/login/?language=en_US&ec=302&startURL=%2Fcustomers%2Fs%2F"
    else:
        raise ValueError("Invalid environment specified")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.maximize_window()

    request.cls.driver = driver

    if country:
        country_variables = COUNTRY_VARIABLES.get(country)
        if not country_variables:
            raise ValueError(f"No variables found for country: {country}")
        request.cls.country_variables = country_variables
        print(f"Country Variables in Fixture: {country_variables}")  # Add debug output
    else:
        raise ValueError("Country not specified")


    yield
    # driver.quit()


@pytest.fixture(scope="class")
def credentials(request):
    password = os.getenv('New_Password')
    return {"password": password}
