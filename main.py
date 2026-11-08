def get_schedule(day):
    if day == "Monday" or day == "Friday":
        schedule = [
            "5:30am wake up",
            "6:00am Breakfast",
            "7:00am Daughters School Drop off",
            "7:20am Gym",
            "8:30am CPA Study",
            "10:00am Work",
            "1:30pm Kids Pickup and lunch",
            "2:00pm back to office",
            "6:30pm dinner",
            "7:30pm Study time",
            "10:30pm Bedtime"
        ]
    else:
        schedule = [
            "5:30am wake up",
            "6:00am Breakfast",
            "7:00am Daughters School Drop off",
            "7:20am Gym",
            "8:30am CPA Study",
            "10:00am Work",
            "5:30pm Kids Pickup",
            "6:00pm dinner",
            "7:30pm Study time",
            "10:30pm Bedtime"
        ]

    return schedule


def show_schedule(day):
    print("schedule for", day)
    for activity in get_schedule(day):
        print(activity)


def search_activities(keyword):
    found = False

    for day in days:
        for activity in get_schedule(day):
            if keyword.lower() in activity.lower():
                print(f"{day}: {activity}")
                found = True

    if not found:
        print("No matching activities found.")


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

short_days = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday"
}

print("1. View a day's schedule")
print("2. Search activities")
choice = input("Choose 1 or 2: ").strip()

if choice == "1":
    day = input("Enter a weekday: ").lower().strip()

    if day in short_days:
        day = short_days[day]
    else:
        day = day.capitalize()

    if day in days:
        show_schedule(day)
    else:
        print("Invalid input. Please enter a valid weekday (Monday to Friday).")

elif choice == "2":
    keyword = input("Enter an activity keyword: ").strip()

    while not keyword:
        print("Please enter a nonempty keyword.")
        keyword = input("Enter an activity keyword: ").strip()

    search_activities(keyword)

else:
    print("Invalid choice. Please enter 1 or 2.")