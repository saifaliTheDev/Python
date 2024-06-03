# Saif Ali - 21304/411704 cs 6Th

# Program to check if the input number is even or odd

def check_even_odd():
    try:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

check_even_odd()
