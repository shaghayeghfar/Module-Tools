
# enum exercise

from dataclasses import dataclass
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


available_operating_systems = sorted({
    laptop.operating_system for laptop in laptops
})

print("Available operating systems:")

for index, operating_system in enumerate(
    available_operating_systems, start=1
):
    print(f"{index}. {operating_system}")

while True:
    try:
        choice = int(input("Choose an operating system by number: "))

        if 1 <= choice <= len(available_operating_systems):
            preferred_operating_system = available_operating_systems[choice - 1]
            break

        print("Please choose a number from the menu.")

    except ValueError:
        print("Please enter a valid number.")


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
