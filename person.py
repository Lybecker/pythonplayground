class Person:
  __slots__ = ("name", "age") # This will restrict the class to only have these two attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age