# Adding a key and value using for loops in a blank dictionary
# 
# The for loop iterates through each element in the list. For the first iteration, word takes the value 'great'.
# Next, the if statement checks if word is in the word_counter dictionary.
# Since it doesn't yet, the statement word_counter[word] = 1 adds great as a key to the dictionary with a value of 1.
# Then, it leaves the if else statement and moves on to the next iteration of the for loop. word now takes the value expectations and repeats the process.
# When the if condition is not met, it is because thatword already exists in the word_counter dictionary, and the statement word_counter[word] = word_counter[word] + 1 increases the count of that word by 1.
# Once the for loop finishes iterating through the list, the for loop is complete.

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(book_title)
print("\n")
print(word_counter)

#Output
['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']


{'sherlock': 1, 'huckleberry': 1, 'adventures': 2, 'holmes': 1, 'the': 2, 'great': 2, 'of': 2, 'hamlet': 1, 'expectations': 1, 'gasby': 1, 'fin': 1}



################ Using get ################
# In this line: word_counter[word] = word_counter.get(word,0) + 1, since the key 'great' doesn't yet exist in the dictionary, get() will return the value 0 and word_counter[word] will be set to 1.
# Once it encounters a word that already exists in word_counter (e.g. the second appearance of 'the'), the value for that key is incremented by 1. On the second appearance of 'the', the key's value would add 1 again, resulting in 2.
# Once the for loop finishes iterating through the list, the for loop is complete.
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word,0) + 1
    #print(word_counter)    
    #print("\n")
print(book_title)
print("\n")
print(word_counter) 


