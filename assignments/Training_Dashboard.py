
# Online Python - IDE, Editor, Compiler, Interpreter
#Extending JSONEncoder:
import datetime

# Dashboard Info
title = "Training Dashboard"
training_title = "Appium with Python"
start_date = datetime.date(2025, 9, 22)
end_date = datetime.date(2025, 10, 13)
trainer_name = "Suresh"
topics = ["Python", "Selenium", "Git", "Appium", "Android", "iOS"]

# Students and Marks
students = ["st1", "st2", "st3"]
marks = {"st1": 10, "st2": 9, "st3": 8}

# Display Dashboard
print("\n" + "=" * 40)
print(f"\t\t{title}\t\t")
print("=" * 40)
print(f"Course Name    : {training_title}")
print(f"Trainer        : {trainer_name}")
print(f"Start Date     : {start_date.strftime('%d-%m-%Y')}")
print(f"End Date       : {end_date.strftime('%d-%m-%Y')}")
print(f"Topics Covered : {', '.join(topics)}")
print("\nStudents & Marks:")

# Display students with marks
for student in students:
    print(f"  {student} --> {marks.get(student, 'N/A')}")

print("=" * 40)