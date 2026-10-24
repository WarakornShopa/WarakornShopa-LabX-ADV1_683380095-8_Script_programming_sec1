
from pathlib import Path

from src.config_parser import ConfigParser
from src.scraper_agent import ScraperAgent
from src.utils import save_data_to_json


BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "configs" / "example_site_config.json"
OUTPUT_PATH = BASE_DIR / "data" / "scraped_products.json"


def main():
    print("=== Agentic Web Scraper ===")

    try:
        config = ConfigParser(CONFIG_PATH).load_config()

        print(f"Start URL: {config['start_url']}")
        print(f"Maximum pages: {config['max_pages']}")

        agent = ScraperAgent(config)
        products = agent.scrape()

        save_data_to_json(products, OUTPUT_PATH)

        print(f"\nScraping completed! Total products: {len(products)}")
        print(f"Output file: {OUTPUT_PATH}")

    except Exception as error:
        print(f"Scraping failed: {error}")
        raise


if __name__ == "__main__":
    main()
