
import time
from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data_models import Product
from src.driver_manager import DriverManager
from src.utils import save_data_to_json


class ScraperAgent:
    """Scrape product information from a website using Selenium."""

    def __init__(self, config):
        self.config = config
        self.driver_manager = DriverManager(headless=True)
        self.driver = None

    def scrape(self):
        """Scrape products from the configured number of pages."""
        products = []
        current_url = self.config["start_url"]
        max_pages = self.config["max_pages"]
        delay = self.config["delay_between_pages"]

        try:
            self.driver = self.driver_manager.start()

            for page_number in range(1, max_pages + 1):
                if not current_url:
                    break

                print(f"\nScraping page {page_number}: {current_url}")
                self.driver.get(current_url)

                try:
                    WebDriverWait(self.driver, 15).until(
                        EC.presence_of_element_located(
                            (
                                By.CSS_SELECTOR,
                                self.config["item_container_selector"],
                            )
                        )
                    )
                except Exception:
                    print("No product containers found on this page.")
                    break

                page_products = self._scrape_current_page()
                products.extend(page_products)

                print(f"Found {len(page_products)} products on this page.")

                if page_number < max_pages:
                    next_url = self._get_next_page_url()

                    if not next_url:
                        print("No next page found.")
                        break

                    current_url = next_url
                    time.sleep(delay)

        finally:
            self.driver_manager.close()

        return products

    def _scrape_current_page(self):
        """Extract product information from the current page."""
        selectors = self.config["item_data_selectors"]
        containers = self.driver.find_elements(
            By.CSS_SELECTOR,
            self.config["item_container_selector"],
        )

        products = []

        for container in containers:
            try:
                name_element = container.find_element(
                    By.CSS_SELECTOR, selectors["name"]
                )
                name = name_element.text.strip()

                price_element = container.find_element(
                    By.CSS_SELECTOR, selectors["price"]
                )
                price = price_element.text.strip()

                url_element = container.find_element(
                    By.CSS_SELECTOR, selectors["url"]
                )
                product_url = url_element.get_attribute("href") or ""
                product_url = urljoin(self.driver.current_url, product_url)

                image_url = ""
                image_selector = selectors.get("image_url")

                if image_selector:
                    try:
                        image_element = container.find_element(
                            By.CSS_SELECTOR, image_selector
                        )
                        image_src = (
                            image_element.get_attribute("src")
                            or image_element.get_attribute("data-src")
                            or ""
                        )
                        image_url = urljoin(
                            self.driver.current_url, image_src
                        ) if image_src else ""
                    except Exception:
                        pass

                description = None
                description_selector = selectors.get("description")

                if description_selector:
                    try:
                        description = container.find_element(
                            By.CSS_SELECTOR, description_selector
                        ).text.strip()
                    except Exception:
                        description = None

                product = Product(
                    name=name,
                    price=price,
                    url=product_url,
                    image_url=image_url,
                    description=description,
                )
                products.append(product.to_dict())

            except Exception as error:
                print(f"Skipping a product because of an error: {error}")

        return products

    def _get_next_page_url(self):
        """Find the URL of the next page, if available."""
        selector = self.config.get("pagination_selector")

        if not selector:
            return None

        try:
            next_link = self.driver.find_element(
                By.CSS_SELECTOR, selector
            )
            href = next_link.get_attribute("href")

            if href:
                return urljoin(self.driver.current_url, href)

        except Exception:
            pass

        return None
