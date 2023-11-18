from collections import UserDict

class Field():
    pass


class Name():
    pass

class Phone(Field):
    def validate(self, value):
        if len(value) < 10 and not value.isdigit():
            raise ValueError("Phone number should be 10 digits long")
        

class Record():
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def __str__(self) -> str:
        pass
    
    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def delete_phone(self, phone_number:str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone in self.phones:
            self.phones.remove(phone)
    
    def edit_phone(self, old_phone:str, new_phone:str):
        old_phone = Phone(old_phone)
        old_phone.validate(old_phone)
        new_phone = Phone(new_phone)
        new_phone.validate(old_phone)
        for i in range(self.phones):
            if self.phones[i] == old_phone:
                self.phones[i] = new_phone


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record 


    def find(self):
        pass

    def delete(self):
        pass