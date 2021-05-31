# 객체지향 프로그래밍 13주차 예제, 회사class 프로그램, 컴퓨터공학과 2학년 1826052 최영서

from Employee import *


def letsWork(company):
    for person in company.Employees:
        person.doWork()
        print(person)


myCompany = Company("삼성")
letsWork(myCompany)