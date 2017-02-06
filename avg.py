#Stephanie Yoon, Angela Yu, Henry Zhang
#SoftDev2 pd8
#HW2 -- You Boys Like Mexico?
#2017-02-07   

from pymongo import MongoClient

c=MongoClient("lisa.stuy.edu", 27017)
ourDB=c.MongoMadness

students = ourDB.find()

for student in students:
    total = 0
    num = 0.0
    for course in grades:
        total += course.value()
        num++
    student['avg'] = total / num
    print student['name']
    print student['id']
    print student['avg']
