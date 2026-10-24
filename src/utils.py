
import json
from pathlib import Path


def save_data_to_json(data, output_path):
    """Save scraped data as a JSON file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Saved {len(data)} products to {output_path}")


def load_data_from_json(input_path):
    """Load previously saved JSON data."""
    input_path = Path(input_path)

    with input_path.open("r", encoding="utf-8") as file:
        return json.load(file)
