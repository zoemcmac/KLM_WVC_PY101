"""
Name: Katherine McAtee
Date: 3/20/2022
Description: A simple program to help manage courses the user is taking.
"""

# Defining list
courses = []


def show_options():
    """
    Display all options and return user's choice
    :return: the user's choice
    """
    menu = """\t Please choose 1 of the following options:
              \t1. List all courses
              \t2. Add a course 
              \t3. Drop a course
              \t4. Sort courses in ascending order of course name
              \t5. Sort courses in descending order of course name
              \t6. Exit\n Enter your option: """
    choice = int(input(menu))
    return choice


# Method for choice one, listing courses
def list_courses():
    """
    Checks if there are any courses listed. If there are, they will be printed out.
    """
    if len(courses) > 0:
        for course in courses:
            print(course)
    else:
        print("Your course list is empty.")


# Method for choice two, adding a course.
def add_course():
    """
    Prompts user for a course to add to the course list.
    """
    new_course = input("Enter the course name:")
    courses.append(new_course)


# Method for choice three, dropping a course.
def drop_course():
    """
    Prompts user for a course name to drop. If it is found in the list, it will be removed.
    If it is not, an error message will be printed.
    """
    remove_course = input("Enter the course name to drop:")
    for i in range(len(courses)):
        if courses[i] != remove_course: continue
        courses.remove(remove_course)
        break
    else:
        print(remove_course, "is not found in your course list.")


# Method for choice four, sorting in ascending order.
def sort_ascending():
    """
    Sorts the courses in course list in ascending alphabetical order of course
    name and prints them.
    """
    if len(courses) > 0:
        # nested loops to sort the list, outer loop iterates through the list, inner loop compares the position of i
        # variable to position of j variable, then switches their positions if i > j
        for i in range(len(courses) - 1):
            for j in range(i + 1, len(courses)):
                if courses[i] > courses[j]:
                    temp = courses[i]
                    courses[i] = courses[j]
                    courses[j] = temp
        print("Course list:")
        for course in courses:
            print(course)
    else:
        print("Your course list is empty.")


def sort_descending():
    """
    Sorts the courses in course list in descending alphabetical order of course
    name and prints them.
    """
    if len(courses) > 0:
        # nested loops to sort the list, outer loop iterates through the list, inner loop compares the position of i
        # variable to position of j variable, then switches their positions if j > i
        for i in range(len(courses) - 1):
            for j in range(i + 1, len(courses)):
                if courses[j] > courses[i]:
                    temp = courses[j]
                    courses[j] = courses[i]
                    courses[i] = temp
        print("Course list:")
        for course in courses:
            print(course)
    else:
        print("Your course list is empty.")


# --------- Main program -----------

# Display the menu and process user's input.
user_choice = 0

# Checks to see if user_choice equals 6, continues loop if it is, exits loop if it is not.
while user_choice != 6:
    # Calls function to show options.
    user_choice = show_options()

    # Checks the input choice value, calls the corresponding method, and returns an error message if entered value is not between 1-6.
    if user_choice == 1:  # Calls function to print out courses.
        list_courses()
    elif user_choice == 2:  # Calls function to add a course.
        add_course()
    elif user_choice == 3:  # Calls function to drop a course.
        drop_course()
    elif user_choice == 4:  # Calls function to sort the classes into ascending order and then print them out.
        sort_ascending()
    elif user_choice == 5:  # Calls function to sort the classes into ascending order and then print them out.
        sort_descending()
    elif user_choice == 6:
        break
    else:
        print("Invalid selection. Please try it again.")
