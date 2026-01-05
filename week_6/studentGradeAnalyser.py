

#task 1.........................................
students_records = []
single_student = ()
unique_score = set()
grad_distribution ={}

n = 1

while n <= 6:
    name = input(f"Enter Name for student {n}: ")
    score = int(input(f"Enter score for student{n}: "))
    n += 1

    single_student = (name , score)
    students_records.append(single_student)


#task 2...............................................
highest_name, highest_score = students_records[0]
lowest_name, lowest_score =students_records[0]
average_score =0
total_score = 0


for name, score in students_records:
    #total score to find avarage
    total_score += score

    #highest and lowest score
    if score > highest_score:
        highest_name, highest_score = name,score

    if score < lowest_score:
        lowest_name, lowest_score = name,score

    #task 3.................................................
    unique_score.add(score)

    #task 4.....................................................
    grad_distribution[score] = grad_distribution.get(score, 0) +1

    # to find average..........>>>>>>>>>>>>>>>>>>>>>>>>>Task 2<<<<<<<<<<<<<<<<<<<<<
average_score = total_score/len(students_records)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>_____printing result______<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print(f"\n========STUDENT RECORD========")
for name, score in students_records:
    print(f"    Name: {name}\n    Score: {score}\n")

print(f"\n========CLASS STATISTICS========")
print(f"    Highest Score: {highest_score}\n    Lowest Score: {lowest_score}\n    Average Score: {average_score}\n")

print(f"\n========UNIQUE SCORES========")
for i in unique_score:
    print(f"    {i}\n")

print(f"\n========GRAD DISTRIBUTION========")
for score,count in grad_distribution.items():
    print(f"    Grad: {score} => {count}\n")





