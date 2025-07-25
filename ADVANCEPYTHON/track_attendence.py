import json
from datetime import date

# A dictionary to store student attendance records
attendance_data = {}

def add_student(name):
    """Add a new student to the attendance record."""
    if name in attendance_data:
        print(f"Student {name} is already in the class.")
    else:
        attendance_data[name] = []
        print(f"Student {name} added to the class.")

def mark_attendance(name, status):
    """Mark attendance for a student."""
    if name not in attendance_data:
        print(f"Student {name} is not in the class. Please add them first.")
        return
    # Store the attendance as a dictionary with the date and status
    attendance_data[name].append({
        'date': str(date.today()),
        'status': status
    })
    print(f"Attendance marked for {name} as {status}.")

def view_attendance(name):
    """View attendance history of a student."""
    if name not in attendance_data:
        print(f"Student {name} is not in the class.")
        return
    print(f"Attendance record for {name}:")
    for record in attendance_data[name]:
        print(f"Date: {record['date']}, Status: {record['status']}")

def save_data(filename="attendance_data.json"):
    """Save attendance data to a file."""
    with open(filename, 'w') as file:
        json.dump(attendance_data, file)
    print("Attendance data saved.")

def load_data(filename="attendance_data.json"):
    """Load attendance data from a file."""
    global attendance_data
    try:
        with open(filename, 'r') as file:
            attendance_data = json.load(file)
        print("Attendance data loaded.")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")

def show_menu():
    """Display menu options."""
    print("\nClassroom Management Tool")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Save Data")
    print("5. Load Data")
    print("6. Exit")

def main():
    load_data()  # Load data on startup
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter student name: ")
            add_student(name)

        elif choice == "2":
            name = input("Enter student name: ")
            status = input("Enter attendance status (present/absent): ").lower()
            if status in ["present", "absent"]:
                mark_attendance(name, status)
            else:
                print("Invalid status. Please enter 'present' or 'absent'.")

        elif choice == "3":
            name = input("Enter student name: ")
            view_attendance(name)

        elif choice == "4":
            save_data()

        elif choice == "5":
            load_data()

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
