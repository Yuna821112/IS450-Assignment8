# My Weekly Schedule Planner

## Main Topic
This is a simple Python program that shows my weekday schedule.

## Description
The user enters a weekday selection-Monday, Tuesday, Wednesday, Thursday, or Friday.
Monday and Friday have different schedules from Tuesday, Wednesday and Thursday due to kids' practice for cheerleading
The program uses a function called show_schedule(day), a list by using [], a loop to print each activity and user input through input()and meaningful output by print()

## How to Run
Open the project in VS code.
Open the terminal.
Type py main.py
Enter a weekday

## Stage 1 
This is my initial version using basic python concepts with minimal AI assistance . I used VS code's autocomplete suggestions(IntelliSendse) while writing the code.  

## Stage 2
I updated my program to accept short weekday names(mon,tue,wed,thu,fri). It also accepts both uppercase and lowercase inputs. I added input validation to show an error message when the user enters an invalid input such as ramdom words, numbers, or weekends (Saturday and Sunday). 

## AI Tool Used
I used Chat GPT to help improve my Python program
I first asked Chat GPT what improvement I can make to my program and it suggested ading input validation. Also I asked how to accept short weekday names and handle uppercase and lowercase input. I accepted the suggestions that I understood and tested them in VS code. I also asked Chat GPT how to update and save my README.md file and how to commit and push my changes to GitHub using VS code.

## Review
I made adjustments when the program did not work correctly. For example, short weekday names like "mon" did not work because the program did no convert them into full weekday names. I added code to convert "mon" to " Monday" and other short names to full names. I tested the program again, and it worked correctly.

## Assignment 9: Dual-Approach Feature Development

### AI Feature: Activity Search

**Purpose:**
Find activities in my weekly schedule without checking each day separately.

**Expected Behavior:**
The user can choose to view a day's schedule or search by activity keyword. The search displays all matching activities with their days and scheduled times, regardless of capitalization. If no activities match, the program displays a clear message. An empty keyword prompts the user to enter a keyword.

This feature will first work with the existing weekday schedules. After both features are merged, it should also search the weekend schedules.

**Planned Test Cases:**

1. Search for `CPA`. The program should display all CPA study activities with their days and times.
2. Search for `cpa`. The results should be the same as searching for `CPA`.
3. Search for `ABCDE`. The program should display a no-matches message.
4. Enter an empty keyword. The program should ask for a nonempty keyword.

**Test Results:**
- CPA and cpa returned the same five weekday CPA study activities.
- abcde displayed "No matching activities found."
- An empty keyword prompted the user to enter a nonempty keyword.
- Choosing option 1 and entering mon displayed the existing Monday schedule.

**AI Use:**
I provided ChatGPT with my feature specification and existing Python code. ChatGPT generated the activity search implementation, including a menu, case-insensitive matching, and empty-keyword validation.

**Code Review:**
The schedule lists were moved into get_schedule() so that both schedule display and activity search could use them. The original day-only input flow was replaced with a menu. The search checks each weekday activity and displays matching results with the day and time.