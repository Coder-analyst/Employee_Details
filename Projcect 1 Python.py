# Function to create a new text file and write employee details into it
def create_employee_file(filename):
    with open(filename, 'w') as file:
        file.write("Name-Age-Employee Number-Mobile Number-Salary-Increment-PostOffice Name-Address-Working-\n")
        print(f"File '{filename}' created successfully.\n")

# Function to add employee details to the file
def add_employee(filename, employee_details):
    with open(filename, 'a') as file:
        file.write(",".join(employee_details) + "\n")
        print(f"Employee details added to '{filename}'.\n")

# Function to display all employee details from the file
def display_employees(filename):
    print("\n--- Employee Details ---")
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.\n")

# Main program
def main():
    filename = "employees.txt"

    # Step 1: Create the file
    create_employee_file(filename)

    # Step 2: Add details of at least 8 employees
    employees = [
        ["John Doe-30-EMP001-1234567890-50000-5000-Manager-ABC Corp-123 Main St-Online"],
        ["Jane Smith-28-EMP002-9876543210-45000-4000-Developer-ABC Corp-456 Elm St-Offline"],
        ["Robert Brown-35-EMP003-1122334455-60000-7000-Designer-XYZ Ltd-789 Oak St-Online"],
        ["Emily White-32-EMP004-2233445566-4800083000-Tester-XYZ Ltd-321 Pine St-Offline"],
        ["Michael Green-29-EMP005-3344556677-52000-6000-Support-ABC Corp-654 Cedar St-Online"],
        ["Sarah Black-31-EMP006-4455667788-47000-3500-HR-XYZ Ltd-987 Birch St-Offline"],
        ["David Clark-33-EMP007-5566778899-49000-4000-Analyst-ABC Corp-159 Spruce St-Online"],
        ["Laura Taylor-26-EMP008-6677889900-46000-2000-Intern-XYZ Ltd-753 Maple St-Offline"]
    ]

    for employee in employees:
        add_employee(filename, employee)

    # Step 3: Display all employees
    display_employees(filename)

# Run the program
if __name__ == "__main__":
    main()
