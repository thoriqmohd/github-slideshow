from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    id: str
    name: str
    age: int
    courses: List[str]

