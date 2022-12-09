'''
Python: Create a Python class called ‘Student’ having ‘name’, ‘age’ as attribute along with a
list having the marks obtained for three subjects.
• Create a constructor to initialize two objects of this class.
• Create a member function called ‘display’ printing the details of a specific object
• Ask user to enter the values for an object through an ‘accept’ member function.
• Display these details.
'''

class Student:
    def __init__(self):
        self.marks = []
    
    def accept(self):
        name = input("Enter name")
        self.name = name
        age = input("Enter age")
        self.age = age
        print("enter marks in 3 subjects")
        for i in range(3):
            self.marks.append(int(input()))
    
    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)

ob1 = Student()
ob2 = Student()
ob1.accept()
ob2.accept()
ob1.display()
ob2.display()


        