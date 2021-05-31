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
    def __init__(self, name):
        self._name = name
        self._employees = list()
        self._getEmployees()

    @property
    def Name(self):
        return self._name

    @property
    def Employees(self):
        return self._employees

    @Employees.setter
    def Employees(self, value):
        self._employees.append(value)

    def _getEmployees(self):
        with open(
            "/mnt/c/Users/dudtj/study/ubuntu/python/학교/2-1 객체지향프로그래밍/13주차/과제/employeeList.txt",
            "r",
            encoding="UTF-8",
        ) as getFile:
            employeeList = getFile.read().split("\n")

        for fileList in employeeList:
            if fileList.endswith("장"):
                teamManager = Manager(fileList)
                self.Employees = teamManager
            else:
                team = fileList
                self.Employees = team
                teamManager.subordinate = team