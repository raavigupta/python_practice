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

