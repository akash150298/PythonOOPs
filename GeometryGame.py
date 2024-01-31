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

pointx = Point(6,7)
rectanglex = Rectangle(Point(1,1), Point(8,8))
pointx.falls_in_rectangle(rectanglex)
