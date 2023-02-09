# write a program to find lowest score in the list ,dont use min function
score = input("enter the score of students: ").split()
for i in range (0,len(score)):
    score[i] = int(score[i])

lowest_score = 0 
for i in score:
    if i > 0:
        lowest_score = i
print(f"your lowest score is {lowest_score}")