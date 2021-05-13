class Mammal(object):
    def __init__(self, name, color):
        self._name = name
        self._color = color

    @property
    def Name(self):
        return self._name

    @property
    def Color(self):
        return self._color

    def Nurse(self):
        print(f"나 {self.Color}{self.Name}은 태어날 때 수유를 합니다.")

    def __str__(self):
        return f"나 {self.Name}은 포유동물로 나의 클래스 타입은 {type(self)}입니다."

    def Cry(self):
        print("나는 포유동물인데 어떻게 우나요??")


class Cat(Mammal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def Meow(self):
        print(f"나 {self.Color} 고양이 {self.Name}은 야옹~ 야옹~ 웁니다. ")

    def Cry(self):
        self.Meow()


class Dog(Mammal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def Bark(self):
        print(f"나 {self.Color} 강아지 {self.Name}은 멍~ 멍~ 짖습니다. ")

    def Cry(self):
        self.Bark()


class Tiger(Mammal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def Cry(self):
        print(f"나 {self.Color} 호랭이 {self.Name}은 곶감을 무서워하며, 어흥~ 어흥~ 웁니다.")


class Lion(Mammal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def Cry(self):
        print(f"나 {self.Color} 사자 {self.Name}은 무서운게 없으며, 어흥~ 어흥~ 웁니다.")


class Liger(Tiger, Lion):
    def __init__(self, name, color):
        super().__init__(name, color)
