'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках
метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго
(желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав
описанный метод.
'''
import time


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        time_delay = [7, 5, 3]
        k = 0
        for i in self.__color:
            print(f'Переключение светафора на {i}')
            time.sleep(time_delay[k])
            k += 1


TrafficLight = TrafficLight()
TrafficLight.running()
'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: 
length (длина), width (ширина). Значения данных атрибутов должны передаваться 
при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод 
расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв 
метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить 
работу метода.
'''


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return (self._length * self._width * self.volume * self.tol) / 1000


class MassCount(Road):
    def __init__(self, _length, _width, volume, tol):
        super().__init__(_length, _width)
        self.volume = volume
        self.tol = tol


r = MassCount(20, 5000, 25, 5)
'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). Последний атрибут должен 
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на 
базе класса Worker. В классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Peter', 'The Great', 'Beekeeper', 100000, 25000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

'''
4.  Реализуйте базовый класс Car. У данного класса должны быть следующие 
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, 
turn(direction), которые должны сообщать, что машина поехала, остановилась, 
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать 
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод 
show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно 
выводиться сообщение о превышении скорости.
'''
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'Машина {self.name} поехала')

    def stop(self):
        return print(f'Машина {self.name} остановилась')

    def turn_right(self):
        return f'Машина {self.name} повернула на право'

    def turn_left(self):
        return f'Машина {self.name} повернула на лево'

    def show_speed(self):
        return f'Текущая скорость машины {self.name} равна {self.speed}'


class TownCar(Car):

    def show_speed(self):
        print(
            f'Текущая скорость городской машины {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенной для городской машины'
        else:
            return f'Скорость {self.name} нормальная для городской машины'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной для рабочей машины'
        else:
            return f'Скорость {self.name} нормальная для рабочей машины'


class PoliceCar(Car):
    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} не является полицейским автомобилем'


lambo = SportCar(100, 'Red', 'Lambo', False)
mini_couper = TownCar(30, 'White', 'Mini-couper', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue', 'Ford', True)
print(lada.turn_left())
print(f'Машина {lambo.turn_right()}, затем {lambo.stop()}')
print(f'{lada.go()} со скростью {lada.show_speed()}')
print(f'{lada.name} цвета {lada.color}')
print(f'Машина {lambo.name} полицейская? {lambo.is_police}')
print(f'Машина {lada.name} полицейская? {lada.is_police}')
print(lambo.show_speed())
print(mini_couper.show_speed())
print(ford.police())
print(ford.show_speed())

'''
6.Реализовать класс Stationery (канцелярская принадлежность). Определить в нем 
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение 
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), 
Handle (маркер). В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого 
экземпляра.
'''
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручку')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())