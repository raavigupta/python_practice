# Practice: Factorials with While Loops
# My Solution
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while number > 1:

    # multiply the product so far by the current number
    product = product * number
    
    # increment current with each iteration until it reaches number
    number -= 1


# print the factorial of number
print(product)
###################################################
# Using for loops 

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here

for x in range(1,number+1):
    print(x)
    product *= x

# print the factorial of number
print("product is "+str(product))

1
2
3
4
5
6
product is 720
