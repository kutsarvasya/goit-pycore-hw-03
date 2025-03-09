from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.16"},
    {"name": "Jane Smith", "birthday": "1990.03.15"},
    {"name": "Jane S", "birthday": "1990.03.22"},
    {"name": "Jane D", "birthday": "1990.03.08"},
]


def get_upcomming_birthdays(users):
    user_birthday = []

    today = datetime.today().date()

    for user in users:
        day_of_birthday = datetime.strptime(
            user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = day_of_birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = day_of_birthday.replace(year=today.year+1)

        days_until_birthday = (birthday_this_year - today).days

        if days_until_birthday <= 7:

            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)

            if birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            user_birthday.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")
            })

    return user_birthday


print("Список привітань на цьому тижні:", get_upcomming_birthdays(users))
