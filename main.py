#!/usr/bin/python3

from storage import storage
from command_handler import execute_command, ExitProgram, InvalidCommandError
from importlib import import_module

import_module('address_book_commands')

def parse_input(user_input: str) -> list:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")

    with storage:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            try:
                print(execute_command(command, args))
            except (ExitProgram, InvalidCommandError) as e:
                print(str(e))
                if isinstance(e, ExitProgram):
                    break


if __name__ == "__main__":
    main()
