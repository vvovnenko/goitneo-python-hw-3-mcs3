from command_handler import command
from address_book import Record
from storage import storage

@command(name='add')
def add_contact(args: list[str]) -> str:
    """Add new contact into book: add Charly 1234567890"""
    contacts = storage.contacts
    name, phone = args
    contacts.add_record(Record(name, phone))
    return "Contact added."

@command(name='change')
def change_contact(args: list[str]) -> str:
    """Add new contacts phone: change Charly 1234567890"""
    contacts = storage.contacts
    name, phone = args
    record = contacts.find(name)
    record.change_phone(phone)
    return "Contact updated."


@command(name='phone')
def get_contact(args: list[str]) -> str:
    """Show contacts phone: phone Charly 1234567890"""
    contacts = storage.contacts
    name, = args
    return contacts.find(name).phone


@command(name='add-birthday')
def add_birthday(args: list[str]) -> str:
    """Add contacts birthday: add-birthday Charly 19.07.1999"""
    contacts = storage.contacts
    name, birthday = args
    contacts.find(name).add_birthday(birthday)
    return "Birthday added"

@command(name='show-birthday')
def show_birthday(args: list[str]) -> str:
    """Show contacts birthday: show-birthday Charly 19.07.1999"""
    contacts = storage.contacts
    name, = args
    birthday = contacts.find(name).birthday
    return str(birthday)

@command(name='birthdays')
def show_birthdays_per_week(args: list[str]) -> str:
    """Show all birthdays in a week period: birthdays"""
    contacts = storage.contacts
    lines = list()
    for weekday, names in contacts.get_birthdays_per_week().items():
        lines.append('{}: {}'.format(weekday, ', '.join(
            map(lambda name: str(name), names))))
    return '\n'.join(lines)


@command(name='all')
def get_all(args: list[str]) -> str:
    """Show all contacts"""
    contacts = storage.contacts
    return str.join('\n', map(lambda item: str(item), contacts.data.values()))
