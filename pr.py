print("An example of the area and perimeter of a rectangle and square.")
# Parent class
class Shape:
  def area(self):
    pass

  def perimeter(self):
    pass

# Child class (Rectangle) inheriting from Shape
class Rectangle(Shape):  # <-- Child class
  # __init__ is known as the constructor
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width
  
  def perimeter(self):
    return 2 * (self.length + self.width)

  def display(self):
    print(f"Length: {self.length}")
    print(f"Width: {self.width}")

# Child class (Square) inheriting from Rectangle
class Square(Rectangle):  # <-- Child class
  def __init__(self, side):
    # Invoking the __init__ of the Rectangle class
    super().__init__(side, side)

# Creating object instances
rect = Rectangle(90, 45)
square = Square(80)

# Calling functions on the objects
rect.display()
print(f"Rectangle - Area: {rect.area()}, Perimeter: {rect.perimeter()}")

square.display()
print(f"Square - Area: {square.area()}, Perimeter: {square.perimeter()}")

print("This is for finding the perimeter of a square or rectangle.")
print("For a square enter the same length for all the lengths.")
print("For a rectangle, opposite angles are equal and the length is greater than the width.")
class Numbers:
    
# Finding the perimeter
    # Initializing (Constructor)
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
    
    def add_numbers(self):
        return self.num1 + self.num2 + self.num3 +self.num4
    
# Enter the three numbers you want to add
num1 = int(input("Enter the length"))
num2 = int(input("Ener the length"))
num3 = int(input("Enter the length"))
num4 = int(input("Enter the length"))

expression = Numbers(num1, num2, num3, num4)
result = expression.add_numbers()
print(f"The perimeter of the polygon is: {result}")


class Rectangle:
    def area(self):
        print("The area of a rectangle is calculated as (Length * Width)")

    def perimeter(self):
        print("The perimeter of a rectangle is calculated as 2(Length) + 2(Width)")

class Square:
    def area(self):
        print("The area of a square is calculated as (Side * Side)")

    def perimeter(self):
        print("The perimeter of a square is calculated as 4(Side)")

class Trapezium:
    def area(self):
        print("The area of a trapezium is calculated as 1/2(a + b)*h")

    def perimeter(self):
        print("The perimeter of a trapezium is calculated based on its sides")

# Polymorphism example
def shape_area(shape):
    shape.area()

def shape_perimeter(shape):
    shape.perimeter()

# Creating objects
r = Rectangle()
s = Square()
t = Trapezium()

# Using the same function for different objects
shape_area(r)
shape_perimeter(r)
shape_area(s)
shape_perimeter(s)
shape_area(t)



class Piano:
    def __init__(self):
        self._piano = "Grand Piano"

    def show_piano(self):
        print("Your piano is:", self._piano)

# Let's create the toy box!
box = Piano()

# We can see the toy using the show_toy method
box.show_piano()



print("For this section we will be subtracting the area of a rectangle from a rectangle larger than it.")

class ShapeDiference:
    def __init__(self):
        self._rectangle = 555 

    def show_rectangle(self):
        print("Area differnce:", self._rectangle)

    def subtract_rectangle(self):
        if self._rectangle > 0:
            self._rectangle -= 333
            print("Yay! You successfully subtracted the area of the two polygons.")
        else:
            print("Error")

# Let's use the cookie jar!
jar = ShapeDiference()

jar.show_rectangle() # Shows 555
jar.subtract_rectangle()  # Subtracts 333 
jar.show_rectangle() # Shows 222 squared cm
    