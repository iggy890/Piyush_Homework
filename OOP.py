"""
Write a program by creating an 'Employee' class having the following methods and print the final salary. 
1 - 'getInfo()' which takes the salary, number of hours of work per day of employee as parameter 
2 - 'AddSal()' which adds $10 to salary of the employee if it is less than $500. 
3 - 'AddWork()' which adds $5 to salary of employee if the number of hours of work per day is more than 6 hours.  

class Employee:
    def __addwork(self):
        if self.number_of_hours >= 6:
            self.salary += 5
    
    def getInfo(self, salary, number_of_hours):
        self.salary = salary
        self.number_of_hours = number_of_hours
        self.salary += (self.number_of_hours - 5) * 5

    def AddSal(self):
        if self.salary < 500:
            self.salary += 10

e = Employee()

e.getInfo(450, 1)
print(f"Salary: {e.salary}")
#self.salary += (self.number_of_hours - 5) * 5

Create a class Rectangle to calculate area and perimeter.
"""
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return (self.width * 2) + (self.length * 2)

rect = Rectangle(5, 5)
print(rect.getArea())
print(rect.getPerimeter())