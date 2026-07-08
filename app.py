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
