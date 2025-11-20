import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.utils import attach

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver=driver))
    browser.config.base_url = 'https://demoqa.com'
    yield browser

    attach.add_video(browser)
    browser.quit()