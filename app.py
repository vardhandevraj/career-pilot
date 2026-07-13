class Student:
    def __init__(self, name, roll_no, branch, year, career_goal):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.year = year
        self.career_goal = career_goal
 
    def display_profile(self):
        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_no}")
        print(f"Branch      : {self.branch}")
        print(f"Year        : {self.year}")
        print(f"Career Goal : {self.career_goal}")
 
 
class StudentProfileManager:
    def __init__(self):
        self.students = []   # list = our simple data structure (array)
 
    def create_profile(self):
        print("===== Create Student Profile =====")
        name = input("Enter Student Name : ").strip()
        roll_no = input("Enter Roll Number : ").strip()
        branch = input("Enter Branch : ").strip()
        year = input("Enter Year : ").strip()
        career_goal = input("Enter Career Goal : ").strip()
 
        if name == "" or roll_no == "":
            print("Name and Roll Number cannot be empty!")
            return
 
        student = Student(name, roll_no, branch, year, career_goal)
        self.students.append(student)
        print("Student Profile Created Successfully!")
 
    def view_profiles(self):
        print("===== Student Profiles =====")
        if len(self.students) == 0:
            print("No student profiles found.")
            return
 
        for index, student in enumerate(self.students, start=1):
            print(f"Student {index}")
            student.display_profile()
 
    def longest_career_goal(self):
        # DSA CONCEPT: Linear Search
        # We scan every student one by one and keep track of the
        # "best so far" (longest career goal). This is a simple
        # O(n) linear search/scan over the list.
        print("== Student with longest career goal description ==")
 
        if len(self.students) == 0:
            print("No student profiles found")
            return
 
        longest_student = self.students[0]
        for student in self.students:
            if len(student.career_goal) > len(longest_student.career_goal):
                longest_student = student
 
        print("Longest career goal belongs to:")
        longest_student.display_profile()
 
 
class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.status = "Pending"
 
    def mark_completed(self):
        self.status = "Completed"
 
    def display_task(self):
        print(f"Task     : {self.title}")
        print(f"Due Date : {self.due_date}")
        print(f"Status   : {self.status}")
 
 
class TaskManager:
    def __init__(self):
        self.tasks = []   # list = our simple data structure (array)
 
    def add_task(self):
        print("===== Add Task =====")
        title = input("Enter Task Title : ").strip()
        due_date = input("Enter Due Date : ").strip()
 
        if title == "":
            print("Task title cannot be empty!")
            return
 
        # DSA CONCEPT: Linear Search
        # Checking for duplicates means walking through the whole
        # list and comparing each title -> O(n) linear search.
        for task in self.tasks:  
            if task.title.lower() == title.lower():
                print("This task already exists!")
                return
 
        task = Task(title, due_date)
        self.tasks.append(task)
        print("Task Added Successfully!")
 
    def view_tasks(self):
        print("===== Task List =====")
        if len(self.tasks) == 0:
            print("No tasks found.")
            return
 
        for index, task in enumerate(self.tasks, start=1):
            print(f"Task {index}")
            task.display_task()
 
    def view_tasks_reversed(self):
        # DSA CONCEPT: Reverse Traversal
        # Instead of sorting, we simply walk the list from the last
        # index down to the first index (i.e. traverse it backwards)
        # to show the most recently added tasks first.
        print("=== Task list (Most recent first) ===")
        if len(self.tasks) == 0:
            print("No tasks found")
            return
 
        reversed_tasks = []
        for i in range(len(self.tasks) - 1, -1, -1):
            reversed_tasks.append(self.tasks[i])
 
        for index, task in enumerate(reversed_tasks, start=1):
            print(f"Task {index}")
            task.display_task()
 
    def complete_task(self):
        self.view_tasks()
        if len(self.tasks) == 0:
            return
 
        task_no = int(input("Enter task number to complete : "))
        if task_no >= 1 and task_no <= len(self.tasks):
            self.tasks[task_no - 1].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
 
class CodingProblem:
    def __init__(self, title, platform, difficulty, status):
        self.title = title
        self.platform = platform
        self.difficulty = difficulty
        self.status = status   # "Solved" or "Unsolved"
 
    def display_problem(self):
        print(f"Problem    : {self.title}")
        print(f"Platform   : {self.platform}")
        print(f"Difficulty : {self.difficulty}")
        print(f"Status     : {self.status}")
 
 
class CodingPracticeManager:
    def __init__(self):
        self.problems = []   # list = our simple data structure (array)
 
    def add_problem(self):
        print("===== Add Coding Problem =====")
        title = input("Enter Problem Title : ").strip()
        platform = input("Enter Platform (LeetCode/HackerRank/etc) : ").strip()
        difficulty = input("Enter Difficulty (Easy/Medium/Hard) : ").strip()
        status = input("Have you solved it? (Solved/Unsolved) : ").strip()
 
        if title == "":
            print("Problem title cannot be empty!")
            return
 
        platform = platform.title()
        difficulty = difficulty.capitalize()
        status = status.capitalize()
 
        problem = CodingProblem(title, platform, difficulty, status)
        self.problems.append(problem)
        print("Coding Problem Added Successfully!")
 
    def view_problems(self):
        print("===== Coding Problem List =====")
        if len(self.problems) == 0:
            print("No coding problems found.")
            return
 
        for index, problem in enumerate(self.problems, start=1):
            print(f"Problem {index}")
            problem.display_problem()
 
    def search_by_platform(self):
        # DSA CONCEPT: Linear Search
        # We scan every problem one by one and check if the platform
        # name contains the search text -> O(n) linear search.
        print("=== Search problems by platform ===")
        if len(self.problems) == 0:
            print("No coding problems found")
            return
 
        search_platform = input("Enter platform (or part of it) : ").strip().lower()
        found_any = False
 
        for index, problem in enumerate(self.problems, start=1):
            if search_platform in problem.platform.lower():
                print(f"\nMatch {index}:")
                problem.display_problem()
                found_any = True
 
        if not found_any:
            print("No problems found on that platform.")
 
    def search_by_difficulty(self):
        # DSA CONCEPT: Linear Search
        # Same scan as above, but an exact match instead of a
        # substring match -> still O(n) linear search.
        print("=== Search problems by difficulty ===")
        if len(self.problems) == 0:
            print("No coding problems found")
            return
 
        search_difficulty = input("Enter difficulty (Easy/Medium/Hard) : ").strip().lower()
        found_any = False
 
        for index, problem in enumerate(self.problems, start=1):
            if problem.difficulty.lower() == search_difficulty:
                print(f"\nMatch {index}:")
                problem.display_problem()
                found_any = True
 
        if not found_any:
            print("No problems found with that difficulty.")
 
    def count_solved(self):
        # DSA CONCEPT: Traversal + Counting
        # We must walk every problem once and tally it up -> O(n),
        # with no early exit possible since we need a full count.
        print("=== Solved vs Unsolved summary ===")
        if len(self.problems) == 0:
            print("No coding problems found")
            return
 
        solved = 0
        unsolved = 0
        for problem in self.problems:
            if problem.status == "Solved":
                solved += 1
            else:
                unsolved += 1
 
        print(f"Total Problems : {len(self.problems)}")
        print(f"Solved         : {solved}")
        print(f"Unsolved       : {unsolved}")
 
def student_menu(profile_manager):
    while True:
        print("===== Student Profile Menu =====")
        print("1. Create Student Profile")
        print("2. View Student Profiles")
        print("3. Find student with longest career goal")
        print("4. Back to Main Menu")
 
        choice = input("Enter your choice : ")
 
        if choice == "1":
            profile_manager.create_profile()
        elif choice == "2":
            profile_manager.view_profiles()
        elif choice == "3":
            profile_manager.longest_career_goal()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
 
 
def task_menu(task_manager):
    while True:
        print("===== Task Manager Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. View Tasks (Most Recent)")
        print("5. Back to Main Menu")
 
        choice = input("Enter your choice : ")
 
        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.complete_task()
        elif choice == "4":
            task_manager.view_tasks_reversed()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

def coding_menu(coding_manager):
    while True:
        print("===== Coding Practice Tracker Menu =====")
        print("1. Add Coding Problem")
        print("2. View Coding Problems")
        print("3. Search by Platform")
        print("4. Search by Difficulty")
        print("5. Solved vs Unsolved Summary")
        print("6. Back to Main Menu")
 
        choice = input("Enter your choice : ")
 
        if choice == "1":
            coding_manager.add_problem()
        elif choice == "2":
            coding_manager.view_problems()
        elif choice == "3":
            coding_manager.search_by_platform()
        elif choice == "4":
            coding_manager.search_by_difficulty()
        elif choice == "5":
            coding_manager.count_solved()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")
 
profile_manager = StudentProfileManager()
task_manager = TaskManager()
coding_manager = CodingPracticeManager()
 
while True:
    print("" + "=" * 40)
    print(" CareerPilot")
    print("=" * 40)
    print("1. Student Profile Module")
    print("2. Task Manager Module")
    print("3. Coding Practice Tracker Module")
    print("4. Exit")
 
    choice = input("Enter your choice : ")
 
    if choice == "1":
        student_menu(profile_manager)
    elif choice == "2":
        task_menu(task_manager)
    elif choice == "3":
        coding_menu(coding_manager)
    elif choice == "4":
        print("Thank you for using CareerPilot.")
        break
    else:
        print("Invalid choice!")