class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
myObject = MyClass(12345, "Hello")

print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())