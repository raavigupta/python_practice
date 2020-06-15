#
#
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for index in range(len(names)):
    usernames=names[index].lower().replace(" ","_")
#     names=names.replace(" ","_")
#     usernames=usernames.append(names)
      print(usernames)
