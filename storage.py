import pickle
from address_book import AddressBook
from util.contacts_generator import populateAddressBook
import constant



class ContactsStorage:
    def __init__(self):
        self.filename = constant.FILE_STORAGE
        self.__book = None

    @property
    def contacts(self) -> AddressBook:
        return self.__book

    def __enter__(self) -> AddressBook:
        try:
            with open(self.filename, "rb") as fh:
                self.__book = pickle.load(fh)
        except FileNotFoundError:
            pass
        finally:
            if not isinstance(self.__book, AddressBook):
                self.__book = AddressBook()
                populateAddressBook(self.__book, 100)
        
        return self.__book

    def __exit__(self, exception_type, exception_value, traceback):
        with open(self.filename, "wb") as fh:
            pickle.dump(self.__book, fh)
        self.__book = None

storage = ContactsStorage()
