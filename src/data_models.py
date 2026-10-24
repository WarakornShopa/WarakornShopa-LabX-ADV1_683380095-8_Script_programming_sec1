
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Product:
    """Represent a scraped product."""

    name: str
    price: str
    url: str
    image_url: str = ""
    description: Optional[str] = None

    def to_dict(self):
        """Convert product data into a dictionary."""
        return asdict(self)
