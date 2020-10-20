# Exercise 1
'''Insert or append a list, Inserting in starting, last or particular position'''

def function_1():
    position_of_element = int(input("Enter Position: "))
    name_of_element = input("Enter book name: ")
    subject.insert(position_of_element-1, name_of_element)

subject =[]

print("1. To Insert in a particular position.")
print("2. To Add new Item into the last.")
print("3. To Add new Item into first.")
print("Press q to quit...")

while True:
    your_choice = input("Enter your choice: ")
    if your_choice=='1':
        try:
            function_1()
        except:
            print("Something went wrong.....Try again please!")
            function_1()

    elif your_choice=='2':
        try:
            name_of_element = input("Enter book name: ")
            subject.append(name_of_element)
        except:
            name_of_element = input("Enter book name: ")
            subject.append(name_of_element)

    elif your_choice=='3':
        try:
            name_of_element = input("Enter book name: ")
            subject.insert(0,name_of_element)
        except:
            name_of_element = input("Enter book name: ")
            subject.insert(0, name_of_element)
    else:
        break

for subject_element in subject:
    print(subject_element)
input()