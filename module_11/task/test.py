
from datetime import datetime,date

value = '22.2.2022'
rr = datetime.strptime(value, "%d.%m.%Y").date()

print(rr.day)