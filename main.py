### Main grading program

# Pre-defining values
grade = False
average_score = False
score_math = 100
score_science = 90
score_english = 95

score_array = [score_english, score_math, score_science]

# Checking for valid scores, making sure they are within range and integers.
try:
    if 0 <= score_math and score_science and score_english <= 100:
        score_valid = True
    else:
        score_valid = False
except:
    print("One or more of the scores are not integers.")
    exit()

if not score_valid:
    print("One or more of the scores are not between 0-100")
    exit()

# Sums all in the array and divides by the number of entries, finding the average.
def array_score_averager():
    average_score = sum(score_array) / len(score_array)
    return average_score

average_score = array_score_averager()
print("Your average score is", average_score)

def score_grader():
    grade_dict = {90: "Grade A", 80: "Grade B", 70: "Grade C", 60: "Grade D", 0: "Grade F"}
    for threshold, grade in grade_dict.items():
        if average_score >= threshold:
            return grade
    print("Averaged score was not between 0-100 somehow???")
    exit()


grade = score_grader()
print(grade)


# def score_grader(grade):
#     if 90 <= average_score <= 100:
#         grade = "Grade A"
#         return grade
    
#     if 80 <= average_score < 90:
#         grade = "Grade B"
#         return grade
    
#     if 70 <= average_score < 80:
#         grade = "Grade C"
#         return grade
    
#     if 60 <= average_score < 70:
#         grade = "Grade D"
#         return grade
    
#     if 0 <= average_score < 60:
#         grade = "Grade F"
#         return grade
    
#     else:
#         print("Averaged score was not between 0-100 somehow???")
#         exit()







