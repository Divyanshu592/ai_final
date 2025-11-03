# Define a class named Student
# This File Is Now Edited By This Line
class Student:
    # Constructor method to initialize object attributes
    def _init_(self, name, age, grade):
        self.name = name      # instance variable
        self.age = age        # instance variable
        self.grade = grade    # instance variable

    # Method to display student details
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

    # Method to check if the student passed or failed
    def check_pass(self):
        if self.grade >= 50:
            print(f"{self.name} has passed 🎉")
        else:
            print(f"{self.name} has failed ❌")

# Create objects (instances) of the Student class
student1 = Student("Alice", 18, 85)
student2 = Student("Bob", 17, 45)

# Access methods using objects
student1.display_info()
student1.check_pass()

print("----------------")

student2.display_info()
student2.check_pass()
