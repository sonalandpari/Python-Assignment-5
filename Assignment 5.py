#Task 1: Create a Dictionary of Student Marks

student_name= {
    "Sonal" : 98,
    "Rahul" : 47,
    "Swarnim":80,
    "Divyanshi": 99,
    "Pari":79,
    "Sandhya": 70,
    "Rajiv":94,
    "Alice" : 85
    }


name = input("Enter the student's name(First letter Capital): ")

if name in student_name:
    print(name+"'s marks:",student_name[name])

else:
    print("Student not found")

#Task 2: Demonstrate List Slicing 

numbers = list(range(1, 11))

first_five = numbers[:5]

reversed_five = first_five[::-1]

print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_five)
