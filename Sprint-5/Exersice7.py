
# Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.

from dataclasses import dataclass
from datetime import date


@dataclass
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()

        years = today.year - self.date_of_birth.year

        had_birthday_this_year = (
            (today.month, today.day)
            >= (self.date_of_birth.month, self.date_of_birth.day)
        )

        age = years if had_birthday_this_year else years - 1

        return age >= 18


imran = Person(
    "Imran",
    date(2008, 8, 6),
    "Ubuntu"
)

print(imran.is_adult())