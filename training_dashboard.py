import datetime
title = "Training Dashboard"
training_title = "Appium with Python"
start_date = datetime.date(2025,9,22)
end_date = datetime.date(2025,10,13)
trainer_name = "Suresh"
topics = list("Python,Selenium, Git,Appium,Android,IOS")
students = tuple("st1,st2,st3")
marks_list = tuple('10,9,8')
marks = {'st1':10, 'st2': 9, 'st3': 8}
# [] () {}
print("\t\t"+title+"\t\t")
print(training_title)
#print(start_date.month + "/" + start_date.day)
print(str(start_date.month) + "/" + str(start_date.day))
print(end_date)
print(trainer_name)
print(topics)
print(students)
print(marks)
#Students: ".,.,.,.,."
#Marks: 10,9,8,5,6
