'''
Documentation:
    Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.

'''

'''
Source Code:
    Author: Frank Emilio Gonzalez Lopez
    Date written: 01/15/2025    
    Assignment: Module 2 Lab - Case Study: if...else and while
    This program should ask the user to enter the student's name, student's last name  and GPA and display if the student qualifies 
    for either the Dean's List or the Honor Roll.
'''



def student_checker():
    print("Student Qualification Checker.\n")

    while True:
        
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()  # Ask for the student's last name

        
        if last_name.upper() == 'ZZZ': # Quit if the last name is 'ZZZ'
            print("Exiting the program")
            break

        
        first_name = input("Enter the student's first name: ").strip() # Ask for the student's first name

        
        try:  # Ask for the student's GPA
            student_gpa = float(input("Enter the student's GPA: ").strip())
        except ValueError:
            print("Invalid GPA. Please enter a valid number.")
            continue

        
        if student_gpa >= 3.5:   # Check qualifications
            print(f"Congratulations, {first_name} {last_name}! You have made the Dean's List.")
        elif student_gpa >= 3.25:
            print(f"Well done, {first_name} {last_name}! You have made the Honor Roll.")
        else:
            print(f"Keep working , {first_name} {last_name}. You are not on the Dean's List or the Honor Roll.")


student_checker() # Run the main function

