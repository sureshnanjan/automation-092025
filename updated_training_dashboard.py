import datetime

title = "Training Dashboard"
training_title = "Appium with Python"
start_date = datetime.date(2025, 9, 22)
end_date = datetime.date(2025, 10, 13)
trainer_name = "Suresh"
topics = "Python,Selenium,Git,Appium,Android,IOS".split(",")  # Proper list
students = "st1,st2,st3".split(",")  # Proper list
marks = {'st1': 10, 'st2': 9, 'st3': 8}

# Print dashboard
print("="*50)
print(f"{title:^50}")  # Centered title
print("="*50)
print(f"Training Title: {training_title}")
print(f"Start Date: {start_date.month}/{start_date.day}/{start_date.year}")
print(f"End Date: {end_date.month}/{end_date.day}/{end_date.year}")
print(f"Trainer Name: {trainer_name}")
print("\nTopics Covered:")
for topic in topics:
    print(f" - {topic}")

print("\nStudents and Marks:")
print(f"{'Student':<10}{'Marks':<5}")
print("-"*20)
for student in students:
    print(f"{student:<10}{marks[student]:<5}")

print("="*50)
