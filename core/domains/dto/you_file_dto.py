import datetime
from dataclasses import dataclass


@dataclass
class YouModelDTO:
    # Specify your fields
    title: str
    description: str
    price: float
    category: int
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        if not self.title:
            raise ValueError("Title cannot be empty")
        if len(self.title) > 255:
            raise ValueError("Title must be less than 255 characters")
        if self.price < 0:
            raise ValueError("Price must be positive")
        if self.category < 1:
            raise ValueError("Category must be positive")
