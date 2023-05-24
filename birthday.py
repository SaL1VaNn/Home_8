from datetime import datetime, timedelta

users = [
    {"name": "John", "birthday": datetime(1990, 5, 12)},
    {"name": "Alice", "birthday": datetime(1985, 8, 20)},
    {"name": "David", "birthday": datetime(1992, 4, 5)},
    {"name": "Sarah", "birthday": datetime(1998, 10, 3)},
    {"name": "Michael", "birthday": datetime(1995, 7, 15)},
]


def get_birthdays_per_week(users):
    today = datetime.today().date()
    start_week = today - timedelta(days=today.weekday())
    end_week = start_week + timedelta(days=6)

    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    for i in range(7):
        current_day = start_week + timedelta(days=i)
        if current_day > end_week:
            break

        user_birth = []
        for user in users:
            birthday = user["birthday"].date()
            if birthday >= current_day and birthday <= end_week:
                user_birth.append(user["name"])

        if user_birth:
            print(f"{weekdays[i]}: {', '.join(user_birth)}")


get_birthdays_per_week(users)


# users = [
#     {"name": "John", "birthday": datetime(1990, 5, 12)},
#     {"name": "Alice", "birthday": datetime(1985, 8, 20)},
#     {"name": "David", "birthday": datetime(1992, 4, 5)},
#     {"name": "Sarah", "birthday": datetime(1998, 10, 3)},
#     {"name": "Michael", "birthday": datetime(1995, 7, 15)},
# ]

# get_birthdays_per_week(users)
