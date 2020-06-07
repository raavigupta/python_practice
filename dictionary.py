#Quiz: Verse Dictionary
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(set(verse_dict))
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = verse_dict.get('breathe')
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict)

# get the first element in the sorted list of keys
print(sorted_keys[0])
print('sorted_keys are'+str(sorted_keys))

# find the element with the highest value in the list of keys
print('length of dictionary is '+str(len(verse_dict)))

for key1,value1 in verse_dict.items():
    for key2,value2 in verse_dict.items():
        if (value2 >= value1):
            maxValue = value2
        else:
            maxValue = value1
print(maxValue)

#another approach
for key1,value1 in verse_dict.items():
    for key2,value2 in verse_dict.items():
       maxValue=max(value1,value2)
       maxKey=max(key1,key2)
print(maxKey,'as max key')
print(maxValue,'as max value')  

#Solution provided below 

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 

#Output provided below 
{'make': 1, 'waiting': 1, 'tired': 1, 'when': 2, 'hating': 1, 'give': 1, 'talk': 1, 'losing': 1, 'look': 1, 'too': 3, 'doubting': 1, 'all': 2, 'be': 1, 'wait': 1, 'you': 6, 'it': 1, 'allowance': 1, 'being': 2, 'by': 1, 'for': 1, 'to': 1, 'men': 1, 'in': 1, 'can': 3, 'about': 2, 'are': 1, 'hated': 1, 'wise': 1, 'your': 1, 'yourself': 1, "don't": 3, 'good': 1, 'way': 1, 'keep': 1, 'if': 3, 'blaming': 1, 'nor': 1, 'but': 1, 'or': 2, 'on': 1, 'not': 1, 'deal': 1, 'trust': 1, 'doubt': 1, 'yet': 1, 'lied': 1, 'lies': 1, 'their': 1, 'theirs': 1, 'and': 3, 'head': 1} 

51
False
about
yourself
