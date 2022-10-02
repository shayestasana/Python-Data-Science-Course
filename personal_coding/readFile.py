#if the file is in same directory then just call by its name 
# and tell in which mode u want to open it
#employee_file = open('employees.txt', 'r')   --> this isn't working here so calling by path

path1= r'C:\Users\sanas\Documents\Python Data Science\Coding Python\personal_coding\employees.txt'
employee_file = open(path1, 'r')  
# 'r' -->  means i just want to read only 
# 'w' --> write
# 'a' --> append  (add new information)
# 'r+' --> read and write

print(employee_file.readable()) #checks if readable file or not
#print(employee_file.read())  #read all data

#print(employee_file.readline()) #reads 1st line individually
#print(employee_file.readline()) #reads 2nd line

#print(employee_file.readlines()) # reads all different lines
#print(employee_file.readlines()[2])  #index 2 in list  --> Pam - Receptionist


for employee in employee_file.readlines():
    print(employee)

employee_file.close()