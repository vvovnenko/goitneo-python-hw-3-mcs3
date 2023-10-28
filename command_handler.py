from address_book import AddressBook, Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f'Input error: {e}'
        except IndexError:
            return 'Incorrect index'
        except KeyError as e:
            return f'Incorrect key: {e}'

    return inner


@input_error
def add_contact(args: list[str], contacts: AddressBook) -> str:
    name, phone = args
    contacts.add_record(Record(name, phone))
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: AddressBook) -> str:
    name, phone = args
    record = contacts.find(name)
    record.change_phone(phone)
    return "Contact updated."


@input_error
def get_contact(args: list[str], contacts: AddressBook) -> str:
    name, = args
    return contacts.find(name).phone


@input_error
def add_birthday(args: list[str], contacts: AddressBook) -> str:
    name, birthday = args
    contacts.find(name).add_birthday(birthday)
    return "Birthday added"


@input_error
def show_birthday(args: list[str], contacts: AddressBook) -> str:
    name, = args
    birthday = contacts.find(name).birthday
    return str(birthday)


def show_birthdays_per_week(args: list[str], contacts: AddressBook) -> str:
    lines = list()
    for weekday, names in contacts.get_birthdays_per_week().items():
        lines.append('{}: {}'.format(weekday, ', '.join(
            map(lambda name: str(name), names))))
    return '\n'.join(lines)


def get_all(args: list[str], contacts: AddressBook) -> str:
    return str.join('\n', map(lambda item: str(item), contacts.data.values()))


def hello(*args, **kwargs) -> str:
    return 'How can I help you?'


class ExitProgram(Exception):
    pass


def exit(*args, **kwargs):
    raise ExitProgram('Good bye!')


HANDLERS = {
    'hello': hello,
    'exit': exit,
    'close': exit,
    'add': add_contact,
    'change': change_contact,
    'phone': get_contact,
    'all': get_all,
    'add-birthday': add_birthday,
    'show-birthday': show_birthday,
    'birthdays': show_birthdays_per_week,
}


class InvalidCommandError(Exception):
    pass


def get_handler(command: str):
    handler = HANDLERS.get(command)
    if handler is None:
        raise InvalidCommandError('Invalid command.')
    return handler
