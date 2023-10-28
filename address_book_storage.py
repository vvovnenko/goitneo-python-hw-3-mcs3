import pickle
from pathlib import Path
from address_book import AddressBook


class AddressBookStorage:
    def __init__(self, filename: str):
        self.filename = filename
        self.book = None

    def __enter__(self) -> AddressBook:
        unpacked = None

        file = Path(self.filename)
        if file.is_file():
            with open(self.filename, "rb") as fh:
                unpacked = pickle.load(fh)

        self.book = unpacked if isinstance(
            unpacked, AddressBook) else AddressBook()
        return self.book

    def __exit__(self, exception_type, exception_value, traceback):
        with open(self.filename, "wb") as fh:
            pickle.dump(self.book, fh)

        self.book = None
