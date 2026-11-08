def show_schedule(day):
    print("schedule for",day)
    if day=="Monday" or day=="Friday":
        schedule=["5:30am wake up", "6:00am Breakfast", "7:00am Daughters School Drop off", "7:20am Gym", "8:30am CPA Study", "10:00am Work", "1:30pm Kids Pickup and lunch", "2:00pm back to office", "6:30pm dinner", "7:30pm Study time", "10:30pm Bedtime"]
    if day=="Tuesday" or day== "Wednesday" or day=="Thursday":
        schedule=["5:30am wake up", "6:00am Breakfast", "7:00am Daughters School Drop off", "7:20am Gym", "8:30am CPA Study", "10:00am Work", "5:30pm Kids Pickup", "6:00pm dinner", "7:30pm Study time", "10:30pm Bedtime"]
    if day=="Saturday": 
        schedule=["8:30am wake up", "9:00am Breakfast", "10:00am CPA study", "12:30pm Lunch", "2:00pm MACC team meeting and working on projects", "5:00pm Grocery shopping", "6:30pm Dinner", "8:00pm Free time", "10:30pm Bedtime"]
    if day=="Sunday": 
        schedule=["8:30am wake up", "9:00am Breakfast", "10:00am CPA study", "12:30pm Lunch", "2:00pm Quality Time with Family", "10:30pm Bedtime"]
    for activity in schedule:
        print(activity)
day=input("enter a schedule:").lower().strip()

short_days = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday",                                                                                                                                                                                                                               
    "sat": "Saturday",
    "sun": "Sunday"
}
if day in short_days:
    day = short_days[day]
else:
    day = day.capitalize()
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
 show_schedule(day)
else:
    print("Invalid input. Please enter a valid day (Monday to Sunday).")