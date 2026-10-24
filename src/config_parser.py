
import json
from pathlib import Path


class ConfigParser:
    """Load and validate scraper configuration from a JSON file."""

    def __init__(self, config_path):
        self.config_path = Path(config_path)

    def load_config(self):
        """Load configuration settings from JSON."""
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        with self.config_path.open("r", encoding="utf-8") as file:
            config = json.load(file)

        self.validate_config(config)
        return config

    @staticmethod
    def validate_config(config):
        """Check that required configuration fields are present."""
        required_fields = [
            "start_url",
            "max_pages",
            "delay_between_pages",
            "item_container_selector",
            "item_data_selectors",
        ]

        for field in required_fields:
            if field not in config:
                raise ValueError(
                    f"Missing required configuration field: {field}"
                )

        if not isinstance(config["max_pages"], int) or config["max_pages"] < 1:
            raise ValueError("max_pages must be an integer greater than 0")

        if config["delay_between_pages"] < 0:
            raise ValueError("delay_between_pages cannot be negative")

        if not isinstance(config["item_data_selectors"], dict):
            raise ValueError("item_data_selectors must be a JSON object")
