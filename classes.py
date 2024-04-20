from collections import UserDict
from congratulation import get_upcoming_birthdays
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Телефон неверного формата")
class Birthday(Field):
    def __init__(self, value):
        try:
            value = datetime.strptime(value, '%d.%m.%Y').date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list = []
        self.birthday = None

    def add_birthday(self, date):
        self.birthday = Birthday((date))

    def add_phone(self, number):
        self.phones.append(Phone(number))
    
    def edit_phone(self, old_number, new_number):
        number = next(num for num in self.phones if num.value == old_number)
        self.phones[self.phones.index(number)] = Phone(new_number)

    def find_phone(self, number):
        number = next(num for num in self.phones if num.value == number)
        return self.phones[self.phones.index(number)]

    def remove_phone(self, number):
        number = next(num for num in self.phones if num.value == number)
        del self.phones[self.phones.index(number)]

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, name):
        self.data.update({name.name.value: name})

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def get_upcoming_birthdays(self):
        birthday_list = []
        for name, record in self.data.items():
            birthday_list.append({"name": name, "birthday": record.birthday.value})
        congratulation = get_upcoming_birthdays(birthday_list)
        return print(congratulation)