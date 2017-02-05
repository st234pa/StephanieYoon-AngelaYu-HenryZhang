#from pymongo import MongoClient
import csv

#c=MongoClient("lisa.stuy.edu", 27017)
#ourDB=c.MongoMadness

peeps = open("peeps.csv")
students=csv.DictReader(peeps)

courses = open("courses.csv")
classes=csv.DictReader(courses)

for student in students:
    #adds grade info to student info from peeps, each code (class) is now a dict key with the value being the mark (grade)
    for course in classes:
        if student["id"]==course["id"]:
            student[course["code"]]=course["mark"]
    #reset cursor? so courses can be iterated again
    courses.seek(0)
    print student

#ourDB.students.insert_many(students)
