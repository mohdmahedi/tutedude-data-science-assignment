import os

EMPLOYEE_FILE = "employee_data.txt"

def add_employee():
    try:
        with open(EMPLOYEE_FILE, "a") as f:
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            salary = input("Enter Salary: ")
            f.write(f"{emp_id},{name},{department},{salary}\n")
            print("Employee added successfully!")
    except Exception as e:
        print("Error adding employee:", e)

def view_employees():
    try:
        if not os.path.exists(EMPLOYEE_FILE):
            print("No employee data found.")
            return

        with open(EMPLOYEE_FILE, "r") as f:
            lines = f.readlines()
            if not lines:
                print("No employee records available.")
                return
            print("\n--- All Employees ---")
            for line in lines:
                emp_id, name, department, salary = line.strip().split(',')
                print(f"ID: {emp_id} | Name: {name} | Dept: {department} | Salary: {salary}")
    except Exception as e:
        print("Error viewing employees:", e)

def search_employee_by_id():
    try:
        search_id = input("Enter Employee ID to search: ")
        found = False

        with open(EMPLOYEE_FILE, "r") as f:
            for line in f:
                emp_id, name, department, salary = line.strip().split(',')
                if emp_id == search_id:
                    print(f"Employee Found - ID: {emp_id} | Name: {name} | Dept: {department} | Salary: {salary}")
                    found = True
                    break
        if not found:
            print("Employee not found.")
    except Exception as e:
        print("Error searching employee:", e)

def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee_by_id()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
