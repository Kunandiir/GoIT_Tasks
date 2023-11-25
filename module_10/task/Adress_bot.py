from collections import UserDict

class MyException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
class Field():
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass

class Phone(Field):

    def __init__(self, value):
        if not len(str(value)) == 10 or not value.isdigit():
            raise MyException(f"Phone number {value} should be 10 digits long")
        super().__init__(value)
        

class Record():
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def __str__(self) -> str:
        return f"Name: {self.name.value}, Phones: {[phone for phone in self.phones]}"
    
    def add_phone(self, phone_number: str):
        try:
            phone = Phone(phone_number)
            if phone not in self.phones:
                self.phones.append(phone.value)
        except MyException as error:
            print(error)

    def delete_phone(self, phone_number:str):
        try:
            phone = Phone(phone_number)
            if phone in self.phones:
                self.phones.remove(phone.value)
        except MyException as error:
            print(error)
    
    def edit_phone(self, old_phone:str, new_phone:str):
        try:
            old_phone = Phone(old_phone)
            new_phone = Phone(new_phone)
            for i in range(self.phones):
                if self.phones[i] == old_phone:
                    self.phones[i] = new_phone
        except MyException as error:
            print(error)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record.phones 


    def find(self, item):
        for name in self.data:
            if name == item:
                return f'Number(s) for {name} is {self.data[name]}'

    def delete(self, item):
        for name in self.data:
            if name == item:
                self.data.pop(name)
                return f'Name {name} deleted from address book'
        


record = Record('John Doe')
record.add_phone('1234567890')
record.add_phone('134253')
address_book = AddressBook()

address_book.add_record(record)

print(address_book)

