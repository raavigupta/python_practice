# Important point to remember
# We use <= instead of the < operator, since it was stated that the upper bound is inclusive. 
# Notice that in each condition, we check if points is in a prize bracket by checking if points is 
# less than or equal to the upper bound; 
# we didn't have to check if it was greater than the lower bound. Let's see why this is the case.


points = 1  # use this input to make your submission

# write your if statement here
if(points>=1 and points<=50):
    result='Congratulations! You won a wooden rabbit!'
elif(points>=51 and points<=150):
    result='Congratulations! You won a no prize!'
elif(points>=151 and points<=180):
    result='Congratulations! You won a wafer-thin mint!'
elif(points>=151 and points<=180):
    result='Congratulations! You won a penguin!'
else:
    result='Oh dear, no prize this time.'
print(result)


#another way 

points = 152  # use this input to make your submission

# write your if statement here
if(points>=1 and points<=50):
    result='Congratulations! You won a {}'.format('wooden rabbit!')
elif(points>=51 and points<=150):
    result='Congratulations! You won a {}'.format('no prize!')
elif(points>=151 and points<=180):
    result='Congratulations! You won a {}'.format('wafer-thin mint!')
elif(points>=151 and points<=180):
    result='Congratulations! You won a {}'.format('penguin!')
else:
    result='Oh dear, no prize this time.'
print(result)

points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)



Another quiz

# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 15
guess = 15

if (guess < answer):
    result = "Oops!  Your guess was too low."
elif (guess > answer):
    result = "Oops!  Your guess was too high."
elif (guess == answer):
    result = "Nice!  Your guess matched the answer!"

print(result)

Nice!  Your guess matched the answer!

# Quiz: Tax Purchase
# Depending on where an individual is from we need to tax them appropriately. 
# The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively. 
# Use this information to take the amount of a purchase and the corresponding 
# state to assure that they are taxed by the right amount.
# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'MN'
purchase_amount = 1000

if (state=='CA'):
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif  (state=='MN'):
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif  (state=='NY'):
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)
