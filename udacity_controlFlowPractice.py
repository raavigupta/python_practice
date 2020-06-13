

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
