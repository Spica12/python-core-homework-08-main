from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    # Реалізуйте тут домашнє завдання
    birthdays = dict()

    days_week = {0:'Monday',
                 1:'Tuesday',
                 2:'Wednesday',
                 3:'Thursday',
                 4:'Friday',
                 5:'Monday',
                 6:'Monday'}

    if users == []:
        return birthdays

    current_date = date.today()
    # current_date = datetime(year=2023, month=12, day=26).date()
    
    next_day = 0
    while next_day <= 6:

        day = current_date + timedelta(days=next_day)
        day_week = day.weekday()

        for user in users:

            user_birthday_date = datetime(day.year,
                                          user['birthday'].month, 
                                          user['birthday'].day).date()
                    
            if user_birthday_date == day:

                try:
                    birthdays[days_week[day_week]].append(user['name'])
                except KeyError:
                    birthdays[days_week[day_week]] = []
                    birthdays[days_week[day_week]].append(user['name'])
                
        next_day += 1

    return birthdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2023, 12, 21).date()},
    ]

    result = get_birthdays_per_week(users)
    # print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
