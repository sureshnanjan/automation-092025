import datetime

# Dashboard info
title = "Training Dashboard"
training_title = "Appium with Python"
start_date = datetime.date(2025, 9, 22)
end_date = datetime.date(2025, 10, 13)
trainer_name = "Suresh"

# Correct data structures
topics = ["Python", "Selenium", "Git", "Appium", "Android", "iOS"]
students = ("st1", "st2", "st3")
marks = {"st1": 10, "st2": 9, "st3": 8}

# Printing dashboard
print("\n" + "="*50)
print(f"\t\t{title}\t\t")
print("="*50)
print(f"Training: {training_title}")
print(f"Trainer : {trainer_name}")
print(f"Duration: {start_date.strftime('%d-%b-%Y')} → {end_date.strftime('%d-%b-%Y')}")
print(f"Topics  : {', '.join(topics)}")
print(f"Students: {', '.join(students)}")
print("-"*50)

# Display marks clearly
print("Student Marks:")
for student, mark in marks.items():
    print(f"  {student}: {mark}")

# Extra operations
print("\n📌 Extra Operations")

# 1. Average marks
average = sum(marks.values()) / len(marks)
print(f"Average Marks: {average:.2f}")

# 2. Highest scorer
top_student = max(marks, key=marks.get)
print(f"Top Performer: {top_student} ({marks[top_student]} marks)")

# 3. Days of training
days = (end_date - start_date).days
print(f"Total Training Days: {days}")

# 4. Check if course has started
today = datetime.date.today()
if today < start_date:
    print("Status: Training has not started yet")
elif start_date <= today <= end_date:
    print("Status: Training is ongoing")
else:
    print("Status: Training completed")
