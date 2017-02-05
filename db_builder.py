from pymongo import MongoClient
import csv

c=MongoClient("lisa.stuy.edu", 27017)
ourDB=c.MongoMadness

peeps = open("peeps.csv")
students=csv.DictReader(peeps)
#ourDB.peeps.insert_one(students)

courses = open("courses.csv")
classes=csv.DictReader(courses)
#ourDB.courses.insert_one(classes)
