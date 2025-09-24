import datetime

# Dashboard Data
title = "Python Training"
training_title = "Appium with Python"
start_date = datetime.date(2025, 9, 22)
end_date = datetime.date(2025, 10, 13)
trainer_name = "Suresh"

topics = ["Python", "Selenium", "Git", "Appium", "Android", "iOS"]
students = ["st1", "st2", "st3"]
marks = {'st1': 10, 'st2': 9, 'st3': 8}

# 10 Best Python Courses
best_courses = [
    "Web Development",
    "Automation",
    "Data Analysis",
    "Machine Learning",
    "Web Data Scraping",
    "IoT",
    "Hacking",
    "Game Development",
    "Computer Vision",
    "Desktop App Development"
]

# Print Header
print("\n" + "=" * 50)
print(f"\t\t{title}")
print("=" * 50)

# Print Training Info
print(f" Training Title : {training_title}")
print(f" Start Date     : {start_date.strftime('%d-%b-%Y')}")
print(f" End Date       : {end_date.strftime('%d-%b-%Y')}")
print(f" Trainer        : {trainer_name}\n")

# Print Topics
print(" Topics Covered :")
for idx, topic in enumerate(topics, start=1):
    print(f"   {idx}. {topic}")
print()

# Students & Marks Table (manual formatting)
print("Student Performance:\n")
print("+----------------+-------+")
print("|   Student      | Marks |")
print("+----------------+-------+")
for student in students:
    print(f"| {student:<14} | {marks[student]:<5} |")
print("+----------------+-------+")

# Best Python Courses
print("10 Best Python Courses:\n")
for idx, course in enumerate(best_courses, start=1):
    print(f"   {idx}. {course}")
print()




