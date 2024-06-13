def is_even(num):
    return num % 2 == 0

def get_number():
    return int(input("Enter a number: "))

def main():
    print("Odd or even checker")
    number = get_number()
    if is_even(number):
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
        
# Run the main function
main()