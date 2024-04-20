from os import name
from classes import AddressBook, Record
from error import input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    print(record)
    return f"{name} contact has been change"

@input_error
def show_phone(args, book):
    name, = args
    record = book.find(name)
    if record is None:
        return "Contact dont find"
    return f"Contact name: {name}, phones: {'; '.join(p.value for p in record.phones)}"
    
@input_error
def show_all(contacts):
    message = ''
    for contact in contacts.items():
        message += f"{contact[1]}\n"
    return "All contacts\n" + message
        

@input_error
def add_birthday(args, book):
    name, date, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact dont find"
    record.add_birthday(date)
    return "Birthday is added"

@input_error
def show_birthday(args, book):
    name, *_= args
    record = book.find(name)
    if record is None:
        return "Contact dont find"
    return f"{name} birthday in {record.birthday}"

@input_error
def birthdays(book):
    message = ''
    for i in book.get_upcoming_birthdays():
        message += f"{i["name"]} congratulation in {i['congratulation']}\n"
    return message