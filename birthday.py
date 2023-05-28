from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    current_date = datetime.now().date()
    start_of_week = current_date - timedelta(days=current_date.weekday())

    birthdays_per_week = {}

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_weekday = start_of_week + timedelta(days=birthday.weekday())

        if birthday_weekday < start_of_week + timedelta(days=7):
            if birthday_weekday not in birthdays_per_week:
                birthdays_per_week[birthday_weekday] = [name]
            else:
                birthdays_per_week[birthday_weekday].append(name)

    for day, names in birthdays_per_week.items():
        weekday = day.strftime("%A")
        names_str = ", ".join(names)
        print(f"{weekday}: {names_str}")


users = [
    {"name": "John", "birthday": datetime(1990, 5, 24)},
    {"name": "Alice", "birthday": datetime(1985, 5, 26)},
    {"name": "David", "birthday": datetime(1992, 5, 28)},
    {"name": "Sarah", "birthday": datetime(1998, 5, 29)},
    {"name": "Michael", "birthday": datetime(1995, 5, 30)},
]


get_birthdays_per_week(users)
