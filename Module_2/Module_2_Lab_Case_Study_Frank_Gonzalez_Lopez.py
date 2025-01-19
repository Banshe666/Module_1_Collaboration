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
    print("Welcome to the Student Qualification Checker.\n")
    
    while True:
        last_name = input("Enter the student's last name Or type zzz to quit: ").strip()  # Ask for the student's last name

        if last_name.upper() == 'ZZZ':  # Quit if the last name is 'ZZZ'
            print("Exiting the program...")
            break
        
        first_name = input("Enter the student's first name: ").strip()  # Ask for the student's first name
        
        gpa = input("Enter the student's GPA: ").strip()  # Ask for the student's GPA
        
        if not gpa.replace('.', '', 1).isdigit():  # Check if GPA is a valid number
            print("GPA must be a valid number. Try again.\n")
            continue
        
        gpa = float(gpa)  # Convert GPA to a float number
        
        if gpa >= 3.5:
            print(f"Congratulations, {first_name} {last_name}! You made the Dean's List")
        elif gpa >= 3.25:
            print(f"Well done, {first_name} {last_name}! You made the Honor Roll")
        else:
            print(f"Don't give up, {first_name} {last_name}.")
        
        

student_checker()  # Run the main function


