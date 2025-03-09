from datetime import datetime
entered_data = input("enter the data format yyyy-mm-dd: ")

def get_days_from_today(date):

    while True:
        try:
            date_object = datetime.strptime(date, "%Y-%m-%d").date()
            break
        except ValueError :
            print("you entered the wrong format")
            date= input("enter the data format yyyy-mm-dd: ")
       
    today = datetime.today().date()
    return((today -date_object).days)
 
print(get_days_from_today(entered_data))
