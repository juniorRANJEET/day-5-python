# Write a program to calculate average height of students which is entered in the list dont use sum function and len function
print("simply write the students height value without comma like 180 200 300 not 200cm 300cm")
print("this program is used to calculate avg height")
h = input("enter the height of students: ").split()
for i in range (0, len(h)):
    h[i] = int(h[i])

total_height = 0
for j in h:
    total_height += j

no_of_students = 0
for k in h:
    no_of_students += 1

avg_height = round(total_height/no_of_students)
print(avg_height)


