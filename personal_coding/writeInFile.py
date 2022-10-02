'''
Jim - Salesman
Dwight - Salesman
Pam - Receptionist
Michael - Manager
Oscar - Accountant
Toby - Human Resources
Kelly - Customer Service
'''



path1= r'C:\Users\sanas\Documents\Python Data Science\Coding Python\personal_coding\employees1.txt'
employee_file = open(path1, 'a') 

# "a" --> append in the existing data at the end
employee_file.write("\nToby - Human Resources") # after run command .. new data is added to the txt file
employee_file.write("\nKelly - Customer Service")

# "w" --> w here, overwrites on the whole the data and only new data remains
#employee_file.write("\nKelly - Customer Service")


employee_file.close()



'''

---creating a new "txt" file from  python code on its own---

employee_file = open('employees3.txt', 'w') 
employee_file.write("\nKelly - Customer Service")
employee_file.close()


---creating a new "html" file from  python code on its own---

employee_file = open('index.html', 'w') 
employee_file.write("<p>This is HTML<p>")
employee_file.close()

'''