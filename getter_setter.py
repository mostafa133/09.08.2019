class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def __str__(self):
        return f'Animal {self.name} {self.__age}'
    '''
    def getAge(self): # getter
        return self.__age
    def setAge(self, value):
        if value >= 0: # setter
            self.__age = value
    '''
    @property
    def age(self):  # getter
        return self.__age
    @age.setter
    def age(self, value):
        if value >= 0:  # setter
            self.__age = value
dolphine = Animal('Lucky', 1.5)
dolphine.age = -200
print(dolphine)
