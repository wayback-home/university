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
        hong = Manager("S123456", "홍길동", "홍보팀")
        self.Employees = hong

        kim = Employee("S123457", "김개똥", "홍보팀")
        self.Employees = kim
        hong.Subodinate = kim

        park = Employee("S123458", "박디비", "홍보팀")
        self.Employees = park
        hong.Subodinate = park

        hong2 = Manager("S123401", "홍길동2", "영업팀")
        self.Employees = hong2

        kim2 = Employee("S123402", "김개똥2", "영업팀")
        self.Employees = kim2
        hong2.Subodinate = kim2

        park2 = Employee("S123403", "박디비2", "영업팀")
        self.Employees = park2
        hong2.Subodinate = park2