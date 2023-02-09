# write a program to find heighest/lowest score in the list ,dont use max or min function
score = input("enter the score of students: ").split()
for i in range (0,len(score)):
    score[i] = int(score[i])

highest_score = 0
for i in score:
    if i > highest_score:
        highest_score = i
print(f"your heighest score is {highest_score}")