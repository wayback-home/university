from Employee import *


def letsWork(company):
    for person in company.Employees:
        person.doWork()
        print(person)


myCompany = Company("삼성")
letsWork(myCompany)