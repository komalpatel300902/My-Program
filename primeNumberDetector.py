# This program detect wether the number is prime or not.

'''
This program work in recursive meathod. 
Each recursion it increment the devisor. 
Divisor divides the actual number and see wheather the remander is 0 or not.
If reminder is 0 then number is not prime and recursion stops. Then new user input is asked.
And with successive increment if the divisor reaches the values of half of the actual number then it is prime.
The logic of above lines is : 
The divisor greater than the half of actual numbers (User Input) will return fractional output and reminder will not be 0.
Hence it will be a prime number.
'''

def prime(num, divisor = 2):
    if num == 0:     # vote of thanks when user quit program
        print("------ Thanks sir ------")
        return 0

    if (divisor == num//2+1 or num in [1,2,3]):  # condition for being prime number
        print(f"{num} is a prime number.")
        return "prime"

    elif (num%divisor) == 0:    # this is condition for not being prime number
        print(f"{num} is not a prime number.")
        return "not prime"

    else:
        prime(num, divisor + 1) # recursion with incrementing the divisor
    
number = 1      # Condition due to which loop runs.
print("Enter 0 for Quiting the program.")
print("Enter Number greater than 0.")
while number:       # When user input is 0 the loop terminates.
    number  = int(input("Enter Number : ")) # Taking User Input.
    prime(number)       # calling a function

