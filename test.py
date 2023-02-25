class Person:
              def __init__(self,name,age,surname):
                      self.name = name
                      self.age = age
                      self.surname = surname


              def __repr__(self):
                            rep = 'Person(' + self.name + ',' + str(self.age) + ','+self.surname+')'
                            return rep
person = Person("John", 20, "Kewruksa")
print(repr(person))