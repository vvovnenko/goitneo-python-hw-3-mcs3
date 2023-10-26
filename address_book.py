from collections import UserDict
import re
from datetime import datetime
from collections import defaultdict
import calendar


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        if not re.match(r'^[a-zA-z]+$', value):
            raise ValueError(f"Invalid name '{value}'")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        if not re.match(r'^\d{10}$', value):
            raise ValueError(f"Invalid phone number '{value}'")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str):
        birthday = datetime.strptime(value, '%d.%m.%Y')
        super().__init__(birthday)

    @property
    def datetime(self) -> datetime:
        return self.value

    def __str__(self):
        return self.value.strftime('%d.%m.%Y')


class Record:
    def __init__(self, name: str, phone: str):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = None

    def change_phone(self, phone: str):
        self.phone = Phone(phone)

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return "Contact name: {}, phone: {}, birthday: {}".format(
            str(self.name), str(self.phone), str(self.birthday))


class AddressBook(UserDict[str, Record]):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data[name]

    def delete(self, name: str):
        del self.data[name]

    def get_birthdays_per_week(self) -> dict[str, list[Name]]:
        congratulations = defaultdict(list)
        today = datetime.today().date()

        for user in self.data.values():
            if user.birthday is None:
                continue

            nex_birthday = user.birthday.datetime.date().replace(year=today.year)

            if (nex_birthday < today):
                nex_birthday = nex_birthday.replace(year=today.year + 1)

            delta_days = (nex_birthday - today).days

            if delta_days >= 7:
                continue

            weekday = nex_birthday.weekday()
            if weekday in [5, 6]:
                weekday = 0

            congratulations[calendar.day_name[weekday]].append(user.name)

        return congratulations

        for weekday, users in congratulations.items():
            print(
                '{}: {}'.format(
                    calendar.day_name[weekday],
                    ', '.join(users)))
