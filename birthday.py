from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime().today().date()
    start_week = today - timedelta(days=today().weekday())
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
            birthdays = user["birthdays"].date()
            if birthdays >= current_day and birthdays <= end_week:
                user_birth.append(user["name"])

            if user_birth:
                print(f"{weekdays[i]}: {', '.join(user_birth)}")
