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

### Manual Feature: Weekend Schedule

**Purpose:**
Extend my weekly schedule planner to include weekend activities, such as CPA study, team project meetings, quality time with my daughters, and grocery shopping.

**Expected Behavior:**
When the user enters Saturday or Sunday, the program displays the schedule for that day. Existing weekday schedules continue to work.

**Planned Test Cases:**

1. Enter `Saturday`. The program should display Saturday’s schedule, including CPA study and a team project meeting.
2. Enter `Sunday`. The program should display Sunday’s schedule, including quality time with my daughters and grocery shopping.
3. Enter `Monday`. The program should continue to display the existing Monday schedule.
4. Enter `Funday`. The program should display an invalid-input message.

**Test Results:**
- Saturday and Sunday displayed the expected weekend schedules.
- Monday displayed the existing weekday schedule.
- Funday displayed the invalid-input message.
- sat and sun displayed the correct weekend schedules.
- Wednesday displayed the existing midweek schedule.