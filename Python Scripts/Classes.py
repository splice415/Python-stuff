# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 17:47:44 2015

@author: Tommy Guan
"""

""" 
    First Example
"""
    class Fruit(object):
        """A class that makes various tasty fruits."""
        def __init__(self, name, color, flavor, poisonous):
            self.name = name
            self.color = color
            self.flavor = flavor
            self.poisonous = poisonous
    
        def description(self):
            print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))
    
        def is_edible(self):
            if not self.poisonous:
                print("Yep! I'm edible.")
            else:
                print("Don't eat me! I am super poisonous.")
    
    lemon = Fruit("lemon", "yellow", "sour", False)
    
    lemon.description()
    lemon.is_edible()
    
"""
Class Instance Object
"""
    class Animal(object):
        def __init__(self, name): #always need __init__ with arg self.
            self.name = name
    
    zebra = Animal("Jeffrey")
    print(zebra.name)

"""
Class Scope
"""
    class Animal(object):
        """Makes cute animals."""
        is_alive = True                 # Member variable, avail for all Animal class
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    zebra = Animal("Jeffrey", 2)
    giraffe = Animal("Bruce", 1)
    panda = Animal("Chad", 7)
    
    print(zebra.name, zebra.age, zebra.is_alive)
    print(giraffe.name, giraffe.age, giraffe.is_alive)
    print(panda.name, panda.age, panda.is_alive)
    
"""
Create Method: description()
"""
    class Animal(object):
        """Makes cute animals."""
        is_alive = True
        def __init__(self, name, age):
            self.name = name
            self.age = age
        # Add your method here!
        def description(self):
            print(self.name)
            print(self.age)
    
    hippo = Animal("Joe", 22)
    hippo.description()

"""
Member Variable: health variable added
"""
    class Animal(object):
        """Makes cute animals."""
        is_alive = True
        health = "good"
        def __init__(self, name, age):
            self.name = name
            self.age = age
        # Add your method here!
        def description(self):
            print(self.name)
            print(self.age)
    
    hippo = Animal("Joe", 22)
    hippo.description()
    
    sloth = Animal("Laze", 5)
    ocelot = Animal("Craze",6)
    print(hippo.health)  #print health of hippo
    print(sloth.health)
    ocelot.health = "bad"
    print(ocelot.health)
    
"""
Shopping Cart class example
"""
    class ShoppingCart(object):
        """Creates shopping cart objects
        for users of our fine website."""
        items_in_cart = {}
        def __init__(self, customer_name):
            self.customer_name = customer_name
    
        def add_item(self, product, price):
            """Add product to the cart."""
            if not product in self.items_in_cart:
                self.items_in_cart[product] = price
                print(product + " added.")
            else:
                print(product + " is already in the cart.")
    
        def remove_item(self, product):
            """Remove product from the cart."""
            if product in self.items_in_cart:
                del self.items_in_cart[product]
                print (product + " removed.")
            else:
                print(product + " is not in the cart.")
    
    my_cart = ShoppingCart("Joe Chan")
    my_cart.add_item("Bugatti", 0.01)
    
"""
Inheritance: a class takes the attributes and methods of another related class.
"""
    # Customer and ReturningCustomer
    class Customer(object):
        """Produces objects that represent customers."""
        def __init__(self, customer_id):
            self.customer_id = customer_id
    
        def display_cart(self):
            print "I'm a string that stands in for the contents of your shopping cart!"
    
    class ReturningCustomer(Customer):
        """For customers of the repeat variety."""
        def display_order_history(self):
            print("I'm a string that stands in for your order history!")
    
    monty_python = ReturningCustomer("ID: 12345")
    monty_python.display_cart()
    monty_python.display_order_history()

# Shape and Triangle
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

"""
Override methods and attributes
"""
    class Employee(object):
        """Models real-life employees!"""
        def __init__(self, employee_name):
            self.employee_name = employee_name
    
        def calculate_wage(self, hours):
            self.hours = hours
            return hours * 20.00
    
    class PartTimeEmployee(Employee):
        """Partimer"""
        def calculate_wage(self, hours):
            self.hours = hours
            return hours*12.00
            
"""
super call to fix override of a parent/superclass method.
"""
    class Employee(object):
        """Models real-life employees!"""
        def __init__(self, employee_name):
            self.employee_name = employee_name
    
        def calculate_wage(self, hours):
            self.hours = hours
            return hours * 20.00
    
    # Add your code below!
    class PartTimeEmployee(Employee):
        def calculate_wage(self, hours):
            self.hours = hours
            return hours*12.00
        
        def full_time_wage(self, hours):
            return super(PartTimeEmployee, self).calculate_wage(hours) 
            # super() uses Employee's calculate_wage's attributes.
    milton = PartTimeEmployee("Milton")
    print(milton.full_time_wage(10))    
    
"""
Triangle Example
"""
    # Create Triangle class
    class Triangle(object):
        def __init__(self, angle1, angle2, angle3):
            self.angle1 = angle1
            self.angle2 = angle2
            self.angle3 = angle3
            
    # Add Member variable and method
    number_of_sides = 3

    def check_angles(self):
        if sum([self.angle1, self.angle2, self.angle3]) == 180:
            return True
        else:
            return False

    #Instantiate an Object
    my_triangle = Triangle(80, 80, 20)
    print(my_triangle.number_of_sides)
    print(my_triangle.check_angles())

    # Create Class Equilateral inheriting Triangle
    class Equilateral(Triangle):
        angle = 60
        
        def __init__(self):
            self.angle1 = self.angle
            self.angle2 = self.angle
            self.angle3 = self.angle
            
"""
Car CLASS
"""
    class Car(object):
        condition = "new"   # member variable
        
        def __init__(self, model, color, mpg):
            self.model = model
            self.color = color
            self.mpg = mpg
    
    model = "DeLorean"
    color = "silver"
    mpg = 88
    
    my_car = Car(model, color, mpg)
    print(my_car.condition)
    print(my_car.model)
    print(my_car.color)
    print(my_car.mpg)

    # Add display_car() method
    class Car(object):
        condition = "new"
        def __init__(self, model, color, mpg):
            self.model = model
            self.color = color
            self.mpg   = mpg
    
        def display_car(self):
            print("This is a %s %s with %s MPG." % (self.color, self.model, self. mpg))
        
    my_car = Car("DeLorean", "silver", 88)
    print(my_car.condition)
    my_car.display_car()
    
    # Change a variable with a method: add drive_car() method
    class Car(object):
        condition = "new"
        def __init__(self, model, color, mpg):
            self.model = model
            self.color = color
            self.mpg   = mpg
    
        def display_car(self):
            print "This is a %s %s with %s MPG." % (self.color, self.model, self. mpg)
        
        def drive_car(self):
            self.condition = "used"
        
    my_car = Car("DeLorean", "silver", 88)
    print my_car.condition
    my_car.drive_car()
    print my_car.condition
    
    # Final
    class Car(object):
        condition = "new"
        def __init__(self, model, color, mpg):
            self.model = model
            self.color = color
            self.mpg   = mpg
    
        def display_car(self):
            print "This is a %s %s with %s MPG." % (self.color, self.model, self. mpg)
        
        def drive_car(self):
            self.condition = "used"
    
    class ElectricCar(Car):
        
        def __init__(self, battery_type, model, color, mpg):
            self.battery_type = battery_type
            super(ElectricCar, self).__init__(model, color, mpg)
            
        def drive_car(self):
            self.condition = "like new"
        
    my_car = ElectricCar("molten salt", "DeLorean", "silver", 88)
    print my_car.condition
    my_car.drive_car()
    print my_car.condition

"""
Point3D
"""
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z
    
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
        
my_point = Point3D(1,2,3)
print my_point