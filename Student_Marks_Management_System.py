# Student Marks Management System

students = {}

while True:
    print("\n--- Student Marks Management ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(f"Name: {name}, Marks: {marks}")

    elif choice == "3":
        search_name = input("Enter student name to search: ")
        if search_name in students:
            print(f"{search_name}'s Marks: {students[search_name]}")
        else:
            print("Student not found.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
