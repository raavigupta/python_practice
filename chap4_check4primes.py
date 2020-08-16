#Coding Quiz: Check for Prime Numbers
## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for prime in  check_prime:
    if (prime %2 == 0):
        print('{} is NOT a prime number, because {} is a factor of {}'.format(prime,2,prime))
    elif (prime %3 == 0):
        print('{} is NOT a prime number, because {} is a factor of {}'.format(prime,3,prime))
    elif (prime %5 == 0):
        print('{} is NOT a prime number, because {} is a factor of {}'.format(prime,5,prime))
    elif (prime %7 == 0):
        print('{} is NOT a prime number, because {} is a factor of {}'.format(prime,7,prime))
    else:
        print('{} is a prime number'.format(prime))

#Output
26 is NOT a prime number, because 2 is a factor of 26
39 is NOT a prime number, because 3 is a factor of 39
51 is NOT a prime number, because 3 is a factor of 51
53 is a prime number
57 is NOT a prime number, because 3 is a factor of 57
79 is a prime number
85 is NOT a prime number, because 5 is a factor of 85

