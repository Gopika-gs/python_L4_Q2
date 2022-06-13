from datetime import date,timedelta


current_date = date.today()
date = current_date - timedelta(5)
print("Subtract five days from current date: " ,date)