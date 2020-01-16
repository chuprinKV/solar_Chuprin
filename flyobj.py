from math import sqrt

# Точность симуляции.
# Чем ниже значение, тем выше точность, но ниже скорость симуляции
T = 1.1

WIN_WIDTH = 1280
WIN_HEIGHT = 720
# Позиция солнца (по центру)
X0 = WIN_WIDTH // 2
Y0 = WIN_HEIGHT // 2
# Масса солнца
M0 = 10000

class FlyObject:
    mass = 0.0
    # v - скорость, a - ускорение
    x, y, vx, vy, ax, ay = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

    # Создание объекта "звезда"
    # Инициализация позиции планеты, скорости и ускорения
    def __init__(self, mass, x, y, vx, vy):
        self.mass = mass
        self.x = x
        self.y = y
        # v - скорость
        self.vx = vx
        self.vy = vy

    def calc(self):
        # r — расстояние между двумя телами
        r = sqrt((self.x - X0) ** 2 + (self.y - Y0) ** 2)
        # a - ускорение
        ax = M0 * (X0 - self.x) / r ** 3
        ay = M0 * (Y0 - self.y) / r ** 3

        # Новая скорость на основе ускорения
        self.vx += T * ax
        self.vy += T * ay

        # Новая позиция на основе скорости
        self.x += T * self.vx
        self.y += T * self.vy

        return r
