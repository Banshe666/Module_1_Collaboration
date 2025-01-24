'''
Documentation:

This application allows users to input details about their vehicle.
It supports various vehicle types such as Car, Semitruck, Motorcycle, or Other.

'''

'''
Source Code:
Author: Frank Emilio Gonzalez L0pez
    Date written: 01/23/2025  
    Assignment: Module 3 Lab - Case Study: Lists, Functions, and Classes
    This application allows users to input details about their vehicle.
    It supports various vehicle types such as Car, Semitruck, Motorcycle, or Other.
    Users are prompted to enter specific attributes based on their vehicle type.
    The information is then stored and displayed in a readable format.

'''

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type  # Type of the vehicle

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)  # Initialize the Vehicle superclass
        self.year = year                
        self.make = make                
        self.model = model              
        self.doors = doors              
        self.roof = roof                

def userCar():
    while True:
        

        # Prompt user to select the type of vehicle
        user_input = input(
            'Please select your type of vehicle:\n'
            '1: Car\n'
            '2: Semitruck\n'
            '3: Motorcycle\n'
            '4: Other\n'
        ).strip()

        if user_input == '1' or user_input.upper() == 'CAR':
            vehicle_type = 'Car'

        elif user_input == '2' or user_input.upper() == 'SEMITRUCK':
            vehicle_type = 'Semitruck'

        elif user_input == '3' or user_input.upper() == 'MOTORCYCLE':
            vehicle_type = 'Motorcycle'

        elif user_input == '4' or user_input.upper() == 'OTHER':
            
            vehicle_type = input('Please specify the type of vehicle you have: ').strip()# Prompt for custom vehicle type
            if not vehicle_type:
                print('That is not a valid input. Please try again.\n')
                continue  # Restart loop if input is invalid

        else:
            print('Please select a valid option.\n')
            continue  # Restart loop if selection is invalid

        print(f'You have selected: {vehicle_type}\n')
        break  # Exit loop after valid selection

   
    year = input("Enter the year of the vehicle: ").strip() # Prompt for additional vehicle details
    make = input("Enter the make of the vehicle: ").strip()
    model = input("Enter the model of the vehicle: ").strip()
    
    while True:
        doors = input("Enter the number of doors (2 or 4): ").strip()
        if doors in ['2', '4']:
            break
        else:
            print("Invalid number of doors. Please enter 2 or 4.\n")
    
    roof = input("Enter the type of roof (solid or sunroof): ").strip().lower()
    if roof not in ['solid', 'sunroof']:
        roof = 'solid'  # Default value if input is invalid

   
    new_car = Automobile(vehicle_type, year, make, model, doors, roof) # Create an instance of Automobile with the provided details

    # Display the vehicle information
    print(f"Vehicle Type: {new_car.vehicle_type}")
    print(f"Year: {new_car.year}")
    print(f"Make: {new_car.make}")
    print(f"Model: {new_car.model}")
    print(f"Number of Doors: {new_car.doors}")
    print(f"Type of Roof: {new_car.roof.capitalize()}")

if __name__ == "__main__": #Run the main instance
    userCar()
