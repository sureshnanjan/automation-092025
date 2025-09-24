Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import datetime
... title = "Training Dashboard"
... training_title = "Appium with Python"
... start_date = datetime.date(2025, 9, 22)
... end_date = datetime.date(2025, 10, 13)
... trainer_name = "Suresh"
... topics = ["Python","Selenium","Git","Appium","Android","iOS."]
... students = ("st1", "st2", "st3")
... marks_list = (10, 9, 8)
... marks = {'st1': 10, 'st2': 9, 'st3': 8}
... print(f"\t\t{title}\t\t")
... print(f"Training Title : {training_title}")
... print(f"Start Date     : {start_date.strftime('%d-%m-%Y')}")
... print(f"End Date       : {end_date.strftime('%d-%m-%Y')}")
... print(f"Trainer Name   : {trainer_name}")
... print("Topics Covered : " + ",".join(topics))
... print("Students registered:")
... for student in students:
...     print(f" {student}")
... print("Marks scored:")
... for student, mark in marks.items():
