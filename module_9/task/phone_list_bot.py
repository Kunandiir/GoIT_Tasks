import re
list_file = "module_9/task/phone_list.txt"

#def input_error(func):

    #def inner(error):
        



#@input_error
def main():

    while True:
        msg =  input("").split(" ")
        if list(map(lambda i: i.lower(), msg))[0] == "hello":
            print(say_hello())
        elif list(map(lambda i: i.lower(), msg))[0] == "add":
            print(add_phone(msg))
        elif list(map(lambda i: i.lower(), msg))[0] == "change":
            print(change_phone(msg))
        elif list(map(lambda i: i.lower(), msg))[0] == "phone":
            print(show_phone(msg))
        elif list(map(lambda i: i.lower(), msg))[0] == "show":
            print(show_all_phones())
        elif list(map(lambda i: i.lower(), msg))[0] in ("good", "close", "exit"):
            print(finish_prog(list(map(lambda i: i.lower(), msg))))
            break
def say_hello():
    return("How can I help you?")

def add_phone(msg):

    if len(msg) == 3:
        with open(list_file, "a") as fl:
            fl.write(msg[1] + ": " + msg[2] + "\n")
            return("contact successfully added")
    else:
        return("input error")


def change_phone(msg):
    if len(msg) == 3:

        with open(list_file, "r+") as fl:
            lines = fl.readlines()
            for i, line in enumerate(lines):
                if re.search(r'^{}:'.format(msg[1]), line):
                    lines[i] = msg[1] + ": " + msg[2] + "\n"
                    fl.seek(0)
                    fl.writelines(lines)
                    return("Phone successfully changed")
            return("value error")
    else:
        return("input error")
        

def show_phone(msg):
     
    if len(msg) == 2:
        with open(list_file, "r+") as fl:
            lines = fl.readlines()
            for i, line in enumerate(lines):
                if re.search(r'^{}:'.format(msg[1]), line) :
                    return("phone for name " + lines[i].split(": ")[0] + " is " + lines[i].split(": ")[1])
        return("value error")
    else:
        return("input error")


def show_all_phones():
    with open(list_file, "r") as fl:
        return("here is all phones in list\n" + "".join(fl.readlines()))

def finish_prog(msg):
    if len(msg) == 2:
        if msg[0] + " " + msg[1] == "good bye":
            return("Good bye!")
        else:
            return("value error")
    return("Good bye!")

main()