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
