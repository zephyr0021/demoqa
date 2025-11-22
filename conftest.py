import os

import pytest
from dotenv import load_dotenv
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.utils import attach

def pytest_addoption(parser):
    parser.addoption(
        '--browser_url',
        default='selenoid.autotests.cloud/wd/hub',
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function')
def setup_browser(request):
    browser_url = request.config.getoption('--browser_url')
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{browser_url}",
        options=options
    )

    browser = Browser(Config(driver=driver))
    browser.config.base_url = 'https://demoqa.com'
    yield browser

    attach.add_video(browser)
    browser.quit()