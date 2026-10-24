
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:
    """Manage the Selenium Chrome WebDriver."""

    def __init__(self, headless=True):
        self.headless = headless
        self.driver = None

    def start(self):
        """Start Chrome and return the WebDriver."""
        options = webdriver.ChromeOptions()

        if self.headless:
            options.add_argument("--headless=new")

        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver

    def close(self):
        """Close the browser safely."""
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
