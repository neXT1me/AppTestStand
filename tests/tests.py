class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

rect = Rectangle(5, 6)
print(rect.area)
# 30 ---9--------18-------27------36---------45------54--------63------72