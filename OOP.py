
class figure:
    def __init__(self, name="cirle", radius=12): # конструктор
        self.name = name
        self.__radius = radius # приватна властивість(моє хехе)

    def __del__(self):  # деструктор
        print('Destructor called, Employee deleted.')


    def Area(self):   # публічна властивість
        return 100 

    def GetFigure(self):    # get figure
        return f"Figure: {self.name}, radius = {self.__radius}, Area = {self.Area()}"


obj1 = figure()
print(obj1.GetFigure())
print("Area:", obj1.Area())
del obj1 # виклик деструктора

