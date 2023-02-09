# Write a program to calculate the odd number summation in a range using range function
print("method 1")
print("Summation of odd number using range function:")
total = 0
for i in range (1,11,2):
    total += i
print(f"The summation of odd number in 0 to 10 is {total}")
print()
print("method 2")
total = 0
print("Summation of odd number using range function:")
for i in range (0,11):
    if i % 2 != 0:
        total +=i
print(f"The summation of odd number in 0 to 10 is {total}")