#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def accept():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_marks = input("Enter student marks: ")
    student_data.append({'id': student_id, 'name': student_name, 'marks': student_marks})
    print("Student added successfully.")

def display():
    if not student_data:
        print("No students found.")
    else:
        for student in student_data:
            print(f"ID: {student['id']}, Name: {student['name']}, Marks: {student['marks']}")

def search():
    search_id = input("Enter student ID to search: ")
    for student in student_data:
        if student['id'] == search_id:
            print(f"ID: {student['id']}, Name: {student['name']}, Marks: {student['marks']}")
            return
        else:
            print("Student not found.")

def delete():
    delete_id = input("Enter student ID to delete: ")
    for student in student_data:
        if student['id'] == delete_id:
            student_data.remove(student)
            print("Student deleted successfully.")
            return
        else:
            print("Student not found.")

def exit():
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    student_data = []

    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            accept()
        elif choice == '2':
            display()
        elif choice == '3':
            search()
        elif choice == '4':
            delete()
        elif choice == '5':
            exit()
        else:
            print("Invalid choice. Please try again.")


# In[ ]:





# In[ ]:




