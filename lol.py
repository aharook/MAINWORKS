class MyClass:

    instance_count = 0  

    def __init__(self):
        MyClass.instance_count += 1  
        self.id = MyClass.instance_count  

    def __str__(self):
        return f"Об'єкт з id = {self.id}"
a = MyClass()
b = MyClass()
c = MyClass()

print(a)  
print(b)  
print(c)  
print("Кількість екземплярів класу:", MyClass.instance_count)
