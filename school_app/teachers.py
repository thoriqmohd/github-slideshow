from dataclasses import dataclass
from typing import List

@dataclass
class Teacher:
    id: str
    name: str
    courses: List[str]

