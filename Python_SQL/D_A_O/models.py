# models.py
from dataclasses import dataclass
from typing import Optional


# так как класс нам нужен лишь для хранения данных, то используем датакласс
@dataclass
class User:
    username: str
    phone: str
    id: Optional[int] = None