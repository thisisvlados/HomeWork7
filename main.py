#1
class soda:
    def __init__(self, _soda: str, taste: str):
        self._soda = _soda
        self.taste = taste

    def sodaluv(self):
        if self.taste == "":
            print("Просто газировка")
        else:
            print(f"Сода имеет вкус: {self.taste=}")

taste = input("Какой сода имеет вкус? ")
taste_1 = soda("Сода", taste)
taste_1.sodaluv()
#2

class Math:

    def __init__(self, a = 10, b = 20):
        self.a = a
        self.b = b
    def addition(self):
        print(self.a + self.b)
    def multiplication(self):
        print(self.a * self.b)
    def division(self):
        print(self.a / self.b)
    def subtraction(self):
        print(self.a - self.b)

x = Math()
x.addition()
x.multiplication()
x.division()
x.subtraction()

#3
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        print('Автомобиль заведён!')
    def end(self):
        print('Автомобиль заглушен!')
    def __repr__(self): #вывод строки
        return (f'{self.color}, {self.type}, {self.year}')

if __name__ == '__main__':
    car_information = Car("Синий", "Легковой", 10)
    print(car_information)
car_information.start()
#4


