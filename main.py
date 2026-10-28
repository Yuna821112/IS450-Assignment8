def show_schedule(day):
    print("schedule for",day)
    if day=="Monday" or day=="Friday":
        schedule=["5:30am wake up", "6:00am Breakfast", "7:00am Daughters School Drop off", "7:20am Gym", "8:30am CPA Study", "10:00am Work", "1:30pm Kids Pickup and lunch", "2:00pm back to office", "6:30pm dinner", "7:30pm Study time", "10:30pm Bedtime"]
    else:
        schedule=["5:30am wake up", "6:00am Breakfast", "7:00am Daughters School Drop off", "7:20am Gym", "8:30am CPA Study", "10:00am Work", "5:30pm Kids Pickup", "6:00pm dinner", "7:30pm Study time", "10:30pm Bedtime"]

    for activity in schedule:
     print(activity)
day=input("enter a weekday:").lower().strip()

short_days = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday"
}
if day in short_days:
    day = short_days[day]
else:
    day = day.capitalize()
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
 show_schedule(day)
else:
    print("Invalid input. Please enter a valid weekday (Monday to Friday).")