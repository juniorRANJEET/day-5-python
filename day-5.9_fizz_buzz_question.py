# Write a program to automatically print the solution for fizz buzz game question for range 1 to 100 :
# where these are the condition :
# if number is completely divisible by 3 ,in place of printing number it comes with fizz
# if number is completely divisible by 5 ,in place of printing number it comes with buzz
# if number is completely divisible by both 3 & 5,in place of printing number it comes with fizz-buzz

print("fizz-buzz game: ")
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz-buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
