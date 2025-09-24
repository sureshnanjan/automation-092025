import datetime

# Training details
title = "Training Dashboard"
training_title = "Appium with Python"
start_date = datetime.date(2025, 9, 22)
end_date = datetime.date(2025, 10, 13)
trainer_name = "Suresh"
topics = ["Python", "Selenium", "Git", "Appium", "Android", "iOS"]
students = ["student_1", "student_2", "student_3"]
marks = {'student_1': 10, 'student_2': 9, 'student_3': 8}

# Header Section
print("="*50)
print(f"{title:^50}")  # Center aligned
print("="*50)
print(f"Training Title : {training_title}")
print(f"Trainer        : {trainer_name}")
print(f"Duration       : {start_date.strftime('%d-%b-%Y')} to {end_date.strftime('%d-%b-%Y')}")
print("-"*50)

# Topics Section
print("Topics Covered:")
for i, t in enumerate(topics, start=1):
    print(f"  {i}. {t}")
print("-"*50)

# Students & Marks (Table)
print("Students Performance:")
print(f"{'Student':<10} | {'Marks':<5}")
print("-"*18)
for s in students:
    print(f"{s:<10} | {marks[s]:<5}")
print("="*50)
