# Saif Ali -21304/411704 cs 6TH

# Program demonstrating the use of while loop with if-else and try-except
def number_operations():
    while True:
        try:
            user_input = input("Enter a number (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                break
            
            number = int(user_input)
            
            if number % 2 == 0:
                print(f"{number} is an even number.")
            else:
                print(f"{number} is an odd number.")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

number_operations()
