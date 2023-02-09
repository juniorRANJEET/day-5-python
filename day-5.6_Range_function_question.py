# for loop with #range function
for number in range (0,11): # here o is incude and 11 would not inclued
    print(number)

print("few more about range function ")
for number in range (0,11,3):
    print(number)

print("few more about range function ")
# addition               # in mathematics formula of summation : n(n+1/2)
total_sum = 0
for i in range (0,11):
    total_sum += i
print(total_sum)

print("few more about range function ")
total_sum = 0
for number in range (0,11,3):
   total_sum += number
print(total_sum)
