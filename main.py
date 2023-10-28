#!/usr/bin/python3

from address_book_storage import AddressBookStorage
from command_handler import get_handler, ExitProgram, InvalidCommandError


def parse_input(user_input: str) -> list:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    storage = AddressBookStorage('_address_book_storage.bin')
    print("Welcome to the assistant bot!")

    with storage as contacts:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            try:
                print(get_handler(command)(args, contacts))
            except (ExitProgram, InvalidCommandError) as e:
                print(str(e))
                if isinstance(e, ExitProgram):
                    break


if __name__ == "__main__":
    main()
