from datetime import datetime,timedelta


user_lst = [
    {"name": "Oleg", "birthday": datetime(year=2024, month=1, day=3)}, #test NewYear dates
    {"name": "Alex", "birthday": datetime.today() + timedelta(days=0)}, 
    {"name": "Oleg", "birthday": datetime.today() + timedelta(days=1)}, 
    {"name": "Sasha", "birthday": datetime.today() + timedelta(days=2)}, 
    {"name": "Nikita", "birthday": datetime.today() + timedelta(days=3)}, 
    {"name": "Gleb", "birthday": datetime.today() + timedelta(days=4)}, 
    {"name": "Maks", "birthday": datetime.today() + timedelta(days=5)}, 
    {"name": "Hulio", "birthday": datetime.today() + timedelta(days=6)}
]
def get_birthdays_per_week(users):
    
    #today = datetime(year=2023, month=12, day=31) #test NewYear dates
    today = datetime.today()
    next_week = today + timedelta(weeks=1)
    birth_users = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday":[],

    }
    for user in users:
        
        user["birthday"] = user["birthday"].replace(year=today.year) #to ignore year
        if user["birthday"].date() <= datetime(year=today.year, month=1, day=7).date(): #NewYear fix
            user["birthday"] = user["birthday"].replace(year=today.year + 1)
        if today.date() <= user["birthday"].date() <= next_week.date():
            
            if user["birthday"].strftime("%A") == "Saturday" or user["birthday"].strftime("%A") == "Sunday":
                birth_users["Monday"].append(user["name"])
            else:
                birth_users[user["birthday"].strftime("%A")].append(user["name"])

    print("\n" + "{:^35}".format("People You Should Congratulate\n"))
    for key, values in birth_users.items():
        if values:
            print("{:^10}|{:^25}".format(key,",".join(values)))




get_birthdays_per_week(user_lst)
