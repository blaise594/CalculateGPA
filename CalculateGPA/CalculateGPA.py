grades = []

continue_entry = True

def user_wants_to_continue():
    return input("Enter another grade? [y/n]:").lower()

# gather grade information
while continue_entry:
    grade = input("Your grade (0.0-4.0): ")
    credits = input("# credits: ")

    # store grades
    grades.append({'grade': float(grade), 'credits': int(credits)})

    user_continue = user_wants_to_continue()
    while user_continue not in ['y', 'n']:
       print("yes or no pls")
       user_continue = user_wants_to_continue()
    if user_continue == 'n':
        continue_entry = False

# compute GPA
total_quality_score = 0
total_credits = 0

# calculate quality scores and total
for grade_info in grades:
    total_quality_score += (grade_info['grade'] * grade_info['credits'])
    total_credits += grade_info['credits']

gpa = total_quality_score / total_credits
print("Your GPA is:", gpa)
