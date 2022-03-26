
print("Welcome to Prime Number Checker")

def prime_checker(number):
    it_is_prime_number = True
    for x in range(2,number):
        if number % x == 0:
            it_is_prime_number = False
    if it_is_prime_number:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

n = int(input("Please provide the number you want to check: "))
prime_checker(number=n)
