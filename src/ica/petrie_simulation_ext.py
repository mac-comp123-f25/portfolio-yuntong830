import random

class Employee:
    def __init__(self, gender, will_comment):
        self.gender = gender
        self.will_comment = will_comment
        self.comments_received = 0

    def __str__(self):
        return (self.gender
                + ": "
                + str(self.comments_received)
                + " sexist comments received (commenter="
                + str(self.will_comment)
                + ")")

    def set_commenter_status(self, status):
        self.will_comment = status

    def receive_sexist_comment(self):
        self.comments_received += 1

    def get_gender(self):
        return self.gender

    def get_commenter_status(self):
        return self.will_comment

    def get_comments_received(self):
        return self.comments_received


def print_employee_list(lst):
    for emp in lst:
        print(emp)


def create_employees(n):
    men_count = int(n * 0.8)
    women_count = n - men_count

    employees = []
    for _ in range(men_count):
        employees.append(Employee("Man", False))
    for _ in range(women_count):
        employees.append(Employee("Woman", False))
    return employees


def create_commenters(employee_list):
    for emp in employee_list:
        if random.random() < 0.2:
            emp.set_commenter_status(True)


def generate_comments(employee_list):
    men = [e for e in employee_list if e.get_gender() == "Man"]
    women = [e for e in employee_list if e.get_gender() == "Woman"]

    for m in men:
        if m.get_commenter_status():
            target = random.choice(women)
            target.receive_sexist_comment()

    for w in women:
        if w.get_commenter_status():
            target = random.choice(men)
            target.receive_sexist_comment()


def average_comments(employee_list):
    male_counts = []
    female_counts = []

    for emp in employee_list:
        if emp.get_gender() == "Man":
            male_counts.append(emp.get_comments_received())
        else:
            female_counts.append(emp.get_comments_received())

    male_avg = sum(male_counts) / len(male_counts)
    female_avg = sum(female_counts) / len(female_counts)

    return male_avg, female_avg


def main():
    employees = create_employees(20)
    create_commenters(employees)
    generate_comments(employees)

    print_employee_list(employees)

    avgs = average_comments(employees)
    print("\nAverage comments (Men, Women):", avgs)