# Student Record Management System using Singly Linked List

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # Add a student
    def add_student(self):
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        new_student = Student(roll_no, name, marks)

        if self.head is None:
            self.head = new_student
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_student

        print("Student added successfully!")

    # Display all students
    def display_students(self):
        if self.head is None:
            print("\nNo student records found.")
            return

        temp = self.head

        print("\n-----------------------------------------")
        print(f"{'Roll No':<10}{'Name':<20}{'Marks':<10}")
        print("-----------------------------------------")

        while temp is not None:
            print(f"{temp.roll_no:<10}{temp.name:<20}{temp.marks:<10}")
            temp = temp.next






   
        print("-----------------------------------------")

    # Search student
    def search_student(self):
        if self.head is None:
            print("\nNo student records found.")
            return

        roll_no = int(input("Enter Roll Number to search: "))

        temp = self.head

        while temp is not None:
            if temp.roll_no == roll_no:
                print("\nStudent Found!")
                print("Roll Number:", temp.roll_no)
                print("Name:", temp.name)
                print("Marks:", temp.marks)
                return

            temp = temp.next

        print("Student not found.")

    # Update student
    def update_student(self):
        if self.head is None:
            print("\nNo student records found.")
            return

        roll_no = int(input("Enter Roll Number to update: "))

        temp = self.head

        while temp is not None:
            if temp.roll_no == roll_no:
                temp.name = input("Enter New Name: ")
                temp.marks = float(input("Enter New Marks: "))

                print("Student record updated successfully!")
                return

            temp = temp.next

        print("Student not found.")

    # Delete student
    def delete_student(self):
        if self.head is None:
            print("\nNo student records found.")
            return

        roll_no = int(input("Enter Roll Number to delete: "))

        # If first node needs to be deleted
        if self.head.roll_no == roll_no:
            self.head = self.head.next
            print("Student deleted successfully!")
            return

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.roll_no == roll_no:
                previous.next = current.next
                print("Student deleted successfully!")
                return

            previous = current
            current = current.next

        print("Student not found.")

    # Sort students
    def sort_students(self):
        if self.head is None or self.head.next is None:
            print("\nNot enough records to sort.")
            return

        print("\nSort By:")
        print("1. Roll Number")
        print("2. Marks")

        choice = int(input("Enter choice: "))

        print("\nOrder:")
        print("1. Ascending")
        print("2. Descending")

        order = int(input("Enter choice: "))

        current = self.head

        while current is not None:
            index = current.next

            while index is not None:

                if choice == 1:
                    if order == 1:
                        condition = current.roll_no > index.roll_no
                    else:
                        condition = current.roll_no < index.roll_no

                elif choice == 2:
                    if order == 1:
                        condition = current.marks > index.marks
                    else:
                        condition = current.marks < index.marks

                else:
                    print("Invalid sorting choice.")
                    return

                if condition:
                    # Swap student data
                    current.roll_no, index.roll_no = \
                        index.roll_no, current.roll_no

                    current.name, index.name = \
                        index.name, current.name

                    current.marks, index.marks = \
                        index.marks, current.marks

                index = index.next

            current = current.next

        print("Records sorted successfully!")


# Main program
students = StudentList()

while True:
    print("\n========== STUDENT RECORD MANAGEMENT ==========")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Sort Students")
    print("6. Display Students")
    print("7. Exit")
    print("===============================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        students.add_student()

    elif choice == 2:
        students.delete_student()

    elif choice == 3:
        students.update_student()

    elif choice == 4:
        students.search_student()

    elif choice == 5:
        students.sort_students()

    elif choice == 6:
        students.display_students()

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
