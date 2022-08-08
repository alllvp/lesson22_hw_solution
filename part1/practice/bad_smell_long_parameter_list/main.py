# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


def get_speed(state):
    if state == 'fly':
        return 1.5
    if state == 'crawl':
        return 1.2
    else:
        return 1


class Unit:

    def __init__(self, x, y):
        self.y = x
        self.x = y

    def move(self, direction, field):
        speed = get_speed()

        if direction == 'UP':
            field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            field.set_unit(y=self.y, x=self.x + speed, unit=self)

