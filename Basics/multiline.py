data = "" # empty string

while True:
    line = input("line >>> ")
    if not line:
        break
    data += line+" "   #stores all the input with a space

print("You have entered following data")
print(data)

# it stores all the input given by the user 
# and it runs until the input is nothing or empty