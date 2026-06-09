students=["Aftab","Pavan","Vishwa","Robin","Bharath"]
#Searching 
has_name=False
search=input("Enter Name to search")
for i in students:
    if (search.lower()==i.lower()):
        has_name=True
        break
if has_name:
    print("student name is available" )     
else:
    print ("Student name is not available")
#number of students    
print("number of students is: ",len(students)) 
#sort names alphabetically 
students.sort()
print(students)
#display first and last name
n=len(students)
print("First student name is ",students[0])
print("last student name is ",students[n-1])
