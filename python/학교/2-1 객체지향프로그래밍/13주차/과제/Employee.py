class Employee(object):
    def __init__(self, idNumber, name, department):
        self._idNumber = idNumber
        self._name = name
        self._department = department

    @property
    def Name(self):
        return self._name

    def doWork(self):
        print(f"나 {self.Name}은 열심히 일을 합니다.")

    def __str__(self):
        return f"나 {self.Name}은 회사원 입니다."


class Manager(Employee):
    def __init__(self, idNumber, name, department):
        super().__init__(idNumber, name, department)
        self._subodinate = list()

    @property
    def Subodinate(self):
        return self._subodinate

    @Subodinate.setter
    def Subodinate(self, value):
        self._subodinate.append(value)

    def doWork(self):
        myteam = list()
        for emplyee in self.Subodinate:
            myteam.append(emplyee.Name)
        print(f"나 {self.Name}은 우리 팀원 {myteam}과 함께 열심히 일을 합니다.")

    def __str__(self):
        return f"나 {self.Name}은 팀장입니다."


class Company:
    employees = list()

    def __init__(self):
        self._getEmployee(
            "/mnt/c/Users/dudtj/study/ubuntu/python/학교/2-1 객체지향프로그래밍/13주차/과제/employeeList.txt"
        )

    @property
    def Name(self):
        return self.name

    @property
    def Employees(self):
        return self.employees

    @Employees.setter
    def Employees(self, value):
        self.employees.append(value)

    def _getEmployee(self, path):
        self._path = path
        name = ""
        idNumber = ""
        position = ""

        with open(path, "r", encoding="UTF-8") as myFile:
            employeeList = myFile.read().split("\n")

            for person in employeeList:
                employee = person.split(",")

                idNumber = employee[0]
                name = employee[1]
                team = employee[2][: len(employee[2]) - 1]
                position = employee[2]

                if position.endswith("장"):
                    employee = Manager(idNumber, name, team)
                else:
                    employee = Employee(idNumber, name, team)

                Company.employees.append(employee)

                for employee in Company.employees:
                    if type(employee) is Manager:
                        for sub in Company.employees:
                            if employee._department == sub._department:
                                employee.SubOrdinate = sub