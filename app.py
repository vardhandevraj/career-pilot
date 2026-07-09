class student:
    def __init__(self, name, roll_no, branch, year, career_goal):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.year = year
        self.career_goal = career_goal
    
    def display_profile(self):
        print("===== Student Profile =====")

        print(f"Name:{self.name}")
        print(f"Roll Number:{self.roll_no}")
        print(f"Branch:{self.branch}")
        print(f"Year:{self.year}")
        print(f"Career Goal:{self.career_goal}")

class studentprofilemanager:
    def __init__(self):
        self.students = []

    def create_profile(self):
        print("\n===== Create Student Profile =====")
        name = input("Enter student name: ")
        roll_no = input("Enter student roll number: ")
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")
        career_goal = input("Enter Career Goal: ")

        if name == "" or roll_no == "":
            print("Error: Name and Roll Number cannot be empty.")
            return
        
        student = student(name, roll_no, branch, year, career_goal) 
        self.students.append(student)
        print("Student profile created successfully!")

def view_profiles(self):
        print("\n===== Student Profiles =====")
        if len(self.students) == 0:
            print("No student profiles found.")
            return
        
        for index, student in enumerate(self.students, start=1):
            print(f"\nStudent {index}")
            student.display_profile()

class task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.status = "Pending"

    def mark_completed(self):
        self.status = "Completed"

    def display_task(self):
        print("===== Task Details =====")
        print(f"Title: {self.title}")
        print(f"Due Date: {self.due_date}")
        print(f"Status: {self.status}")

class taskmanager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        print("\n===== Add Task =====")
        title = input("Enter Task Title: ")
        due_date = input("Enter Due Date: ")

        if title == "" or due_date == "":
            print("Error: Title and Due Date cannot be empty.")
            return
        
        task = task(title, due_date)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        print("\n===== Task List =====")
        if len(self.tasks) == 0:
            print("No tasks found.")
            return
        
        for index, task in enumerate(self.tasks, start=1):
            print(f"\nTask {index}")
            task.display_task()

    def complete_task(self):
        self.view_tasks()
        if len(self.tasks) == 0:
            return
        
    task_no = input("Enter Task Number to Completed: ")
    if task_no >= 1 and task_no <= len(self.tasks):
        task = self.tasks[task_no - 1]
        task.mark_completed()
        print("Task marked as completed!")
    else:
        print("Invalid task number.")
    
def student_menu(profile_manager):
    while True:
        print("\n===== Student Menu =====")
        print("1. Create Student Profile")
        print("2. View Student Profiles")
        print("3. Update Student Profile")
        print("4. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            profile_manager.create_profile()
        elif choice == "2":
            profile_manager.view_profiles()
        elif choice == "3":
            profile_manager.update_profile()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def task_menu(task_manager):
    while True:
        print("\n===== Task Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.complete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
