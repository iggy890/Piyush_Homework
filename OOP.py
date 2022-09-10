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

Homework:
• The Matrix class has methods for each of the following:
	1 - get the number of rows
	2 - get the number of columns
	3 - set the elements of the matrix at given position (I, j)
	4 - adding two matrices. If the matrices are not addable, "Matrices cannot be added" will be displayed.
5 - multiplying the two matrices

class Matrix:
    def __init__(self, rows: list, columns: list) -> None:
        self.rows = rows
        self.columns = columns

        self.num_rows = len(rows)
        self.num_columns = len(columns)

    def get_rows(self) -> int:
        return self.num_rows

    def get_columns(self) -> int:
        return self.num_columns

    def set_element(self, row_index, column_index, row_value, column_value):
        self.rows[row_index] = row_value
        self.columns[column_index] = column_value

    def add_matrix(self, matrix) -> None:
        rows = self.rows + matrix.rows
        columns = self.columns + matrix.columns

        return Matrix(rows, columns)

    def multiply_matrix(self, matrix):
        new_matrix = Matrix([], [])

        rows = new_matrix.rows
        columns = new_matrix.columns

        rows_zip = zip(self.rows, matrix.rows)
        columns_zip = zip(self.columns, matrix.columns)

        for self_rows, matrix_rows in rows_zip:
            for self_columns, matrix_columns in columns_zip:
                rows.append(self_rows * matrix_rows)
                columns.append(self_columns * matrix_columns)

        return new_matrix

new_matrix = Matrix([1, 2], [2, 3])
print(f"columns: {new_matrix.get_columns()}")
print(f"rows: {new_matrix.get_rows()}")

Ninety-Nine Bottles” is a folk song of undetermined origin known for its length  
and repetitiveness. The lyrics go, “Ninety- nine bottles of milk on the wall, ninety-nine  
bottles of milk. Take one down, pass it around, ninety- eight bottles of milk on the wall.” As the lyrics repeat, the number of bottles falls from ninety-eight to ninety- seven, then from ninety-seven to ninety-six, until it  
reaches zero: “One bottle of milk on the wall, one bottle of milk. Take it down, pass it around, no more bottles of milk on the wall!”  
 
Sample Output: 
99 bottles of milk on the wall, 
             99 bottles of milk, 
             Take one down, pass it around, 
             98 bottles of milk on the wall! 
 
98 bottles of milk on the wall, 98 bottles of milk, 
Take one down, pass it around, 97 bottles of milk on the wall!  
… 
1 bottle of milk on the wall! 
1 bottle of milk, 
take it down, pass it around, 
No more bottles of milk on the wall! 
 
Hint: 
The repetition in this song makes it easy to use a for loop to display the first 98 stanzas. However, the last stanza has some minor differences and requires separate code to display This is because the last line 
 'No more bottles of milk on the wall!', 
 deviates from the line repeated in the loop, and because the word “bottle” is singular rather than plural.  

for i in range(100, 1, -1):
    print(f"{i} bottles of milk on the wall,")
    print(f"{i} bottles of milk,")
    print("Take one down pass it around,")
    print(f"{i - 1} bottles of milk on the wall!")

print("1 bottle of milk on the wall,")
print("1 bottle of milk",)
print("Take it down, pass it around")
print("No more bottles of milk on the wall!")

__doc__ can show documentation for classes and methods. __doc__ is also useful for having a look at quick documentation, rather than having a look at the online documentation.
"""
