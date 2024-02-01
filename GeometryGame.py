from random import randint

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def falls_in_rectangle(self, rectangle):
    if rectangle.leftUp.x < self.x \
    < rectangle.rightUp.x \
    and rectangle.leftUp.y < self.y \
    < rectangle.rightUp.y:
      return True
    else:
      return False

class Rectangle:
  def __init__(self, leftUp, rightUp):
    self.leftUp = leftUp
    self.rightUp = rightUp

rectangle = Rectangle(Point(randint(0,9), randint(0,9)), Point(randint(10,17), randint(10,17) ))

print("Rectangle Coordinates: ", rectangle.leftup.x, "," rectangle.leftup.y, "and", rectangle.rightup.x, "," rectangle.rightup.y)

user_point = Point(float(input("Guess x : ")), float(input("Guess y : ")))

print("The point was inside the rectangle", user_point.falls_in_rectangle(rectangle))
