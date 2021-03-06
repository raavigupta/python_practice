# My code
# Using replace 
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for index in range(len(names)):
    username=names[index].lower().replace(" ","_")
    usernames.insert(index,username)
#     names=names.replace(" ","_")
#     usernames=usernames.append(names)
print(usernames)


# My code : Another approach without using range
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
# My code
# write your for loop here
for name in names:
    name=name.lower().replace(" ","_")
    usernames.append(name)
#     usernames=name.append()
#     names=names.replace(" ","_")
#     usernames=usernames.append(names)
print(usernames)

# Output : ['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']

#Provided Solution 

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)

#Provided Solution using Range 
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)
