x= "SOPHOMORE" #negative indexing (-9,-8, -7, -6, -5, -4, -3, -2, -1)
#   012345678  => positive indexing
print(x[2])
print(x[1])
print(x[-3])
print(x[-1])
print(x[-9])
#print(x[-10])  => String not found

str="digipodium"
#    0123456789
# - 10987654321 
print('str = ', str)

print('str[0] = ', str[0])
print('str[1] = ', str[1])
print('str[-1] = ', str[-1])  #last character
print('str[-2] = ', str[-2]) #second last character


# String Slicing "str[m:n]"" eturns the portion of str strating with position m, and upto but not including n

slice2= str[0:4]
print(slice2)
slice1= str[4:7]
print(slice1)
slice3= str[:4]  #same as str[0:4]
print(slice3)

slice6= str[-2:-8]  #doesn't work on negative indexes when they are written in inverse form  -8:-2 then its correct
print(slice6)
slice7= str[-4:]
print(slice7)
slice8= str[-8:-2]
print(slice8)

slice4= str[4:len(str)]
print(slice4)
slice5= str[4:]
print(slice5)