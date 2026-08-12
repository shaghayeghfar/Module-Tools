
#enum exersice

from dataclasses import dataclass
from typing import List
import sys


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: str


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: str


laptops = [
    Laptop(1, "Dell", "XPS", 13, "Ubuntu"),
    Laptop(2, "Dell", "XPS", 15, "Ubuntu"),
    Laptop(3, "Dell", "XPS", 15, "Arch Linux"),
    Laptop(4, "Apple", "MacBook", 13, "macOS"),
    Laptop(5, "Lenovo", "ThinkPad", 14, "Ubuntu"),
]


name = input("Enter your name: ")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Error: age must be a number.", file=sys.stderr)
    sys.exit(1)


preferred_operating_system = input(
    "Enter your preferred operating system: "
)

available_operating_systems = {
    laptop.operating_system for laptop in laptops
}

if preferred_operating_system not in available_operating_systems:
    print(
        "Error: that operating system is not available.",
        file=sys.stderr
    )
    sys.exit(1)


person = Person(
    name=name,
    age=age,
    preferred_operating_system=preferred_operating_system
)


matching_laptops = [
    laptop
    for laptop in laptops
    if laptop.operating_system == person.preferred_operating_system
]

print(
    f"The library has {len(matching_laptops)} "
    f"laptop(s) with {person.preferred_operating_system}."
)


laptop_counts = {}

for laptop in laptops:
    laptop_counts[laptop.operating_system] = (
        laptop_counts.get(laptop.operating_system, 0) + 1
    )


for operating_system, count in laptop_counts.items():
    if (
        operating_system != person.preferred_operating_system
        and count > len(matching_laptops)
    ):
        print(
            f"The library has more {operating_system} laptops "
            f"({count}). You are more likely to get a laptop "
            f"if you are willing to use {operating_system}."
        )