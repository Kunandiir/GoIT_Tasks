from collections import UserDict
from datetime import datetime,date
import json
import atexit



class MyException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Field():
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

class Name(Field):
    pass

class Phone(Field):

    @Field.value.setter
    def value(self, value):
        if not len(str(value)) == 10 or not value.isdigit():
            raise MyException(f"Phone number {value} should be 10 digits long")
        else:
            self._value = value

class Birthday(Field):

    @Field.value.setter
    def value(self, value):
        if value != None:
            if datetime.today().date() >= datetime.strptime(value, "%d.%m.%Y").date():
                self._value = datetime.strptime(value, "%d.%m.%Y").date()
            else:
                raise MyException(f"Incorect birthday date, use format dd.mm.yy")
class Record():
    def __init__(self, name, birthday = None) -> None:
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

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

    def days_to_birthday(self):
        if self.birthday == None:
            raise MyException('No birthday found')
        else:
            next_birthday = datetime(datetime.today().year, self.birthday.value.month, self.birthday.value.day)
            if next_birthday < datetime.today():
                next_birthday = datetime(datetime.today().year + 1, self.birthday.value.month, self.birthday.value.day)
            return (next_birthday - datetime.today()).days
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record.phones 


    def find(self, item):
        nums_lst = []
        for name in self.data:
            if item in name:
                nums_lst.append(f'Number(s) for {name} is {self.data[name]}') 
            else:
                for num in self.data[name]:
                    if item in num: 
                        nums_lst.append(f'Number(s) for {name} is {self.data[name]}') 

        return "\n".join(nums_lst)


    def delete(self, item):
        for name in self.data:
            if name == item:
                self.data.pop(name)
                return f'Name {name} deleted from address book'
    
    def iterator(self, number):
        count = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {record} \n'
            count += 1
            if count >= number:
                return result
    

    def dump(self, path = "module_12/task/AddressBook.json"):
        with open(path, 'w') as fl:
            json.dump(self.data, fl)

    
    def load(self, path = "module_12/task/AddressBook.json"):
        try:
            with open(path, 'r') as fl:
                self.data = json.load(fl)
        except:
            pass



if __name__=='__main__':
    address_book = AddressBook()
    address_book.load()
    atexit.register(address_book.dump)





print(address_book)
print(address_book.find('123'))
'''
record = Record('John Doe', '22.2.2022')
record.add_phone('1234567890')
record.add_phone('1342535465')
record2 = Record('Alex Hirsh')
record2.add_phone('1234666890')

address_book.add_record(record)
address_book.add_record(record2)
#print(address_book.delete('John Doe'))
print(record.days_to_birthday())
address_book.dump()
print(address_book.iterator(2))
print(')' *10)
print(address_book)
'''