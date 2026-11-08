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
    elif day in ["Tuesday", "Wednesday", "Thursday"]:
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
    elif day == "Saturday":
        schedule = [
            "8:30am wake up",
            "9:00am Breakfast",
            "10:00am CPA study",
            "12:30pm Lunch",
            "2:00pm MACC team meeting and working on projects",
            "5:00pm Grocery shopping",
            "6:30pm Dinner",
            "8:00pm Free time",
            "10:30pm Bedtime"
        ]
    elif day == "Sunday":
        schedule = [
            "8:30am wake up",
            "9:00am Breakfast",
            "10:00am CPA study",
            "12:30pm Lunch",
            "2:00pm Quality Time with Family",
            "10:30pm Bedtime"
        ]
    else:
        schedule = []

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


days = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
]

short_days = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday",
    "sat": "Saturday",
    "sun": "Sunday"
}

print("1. View a day's schedule")
print("2. Search activities")
choice = input("Choose 1 or 2: ").strip()

if choice == "1":
    day = input("Enter a day (Monday to Sunday): ").lower().strip()

    if day in short_days:
        day = short_days[day]
    else:
        day = day.capitalize()

    if day in days:
        show_schedule(day)
    else:
        print("Invalid input. Please enter a valid day (Monday to Sunday).")

elif choice == "2":
    keyword = input("Enter an activity keyword: ").strip()

    while not keyword:
        print("Please enter a nonempty keyword.")
        keyword = input("Enter an activity keyword: ").strip()

    search_activities(keyword)

else:
    print("Invalid choice. Please enter 1 or 2.")