##############
# My solution
##############

limit = 40

number = 1
nearest_square = 1
print(nearest_square)
# write your while loop here
while (nearest_square <= limit):
    number = number + 1
    square = number * number # 49
    nearest_square = square # 49
    if(nearest_square > limit):
        break
print(number)
nearest_square = (number-1) * (number-1)
print(nearest_square)

##############
# Solution
##############
limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)
