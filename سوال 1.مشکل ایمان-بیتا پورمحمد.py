def calculate_grade(n, exams):
    # دیکشنری برای تبدیل نمرات به مقادیر عددی
    grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    
    total_weighted_score = 0
    total_weight = 0
    
    for exam in exams:
        weight, grade = exam
        score = grade_points[grade]
        total_weighted_score += weight * score
        total_weight += weight
    
    # محاسبه میانگین وزنی
    if total_weight == 0:
        return 'F'  # اگر هیچ وزنی وجود نداشته باشد، نمره F است
    weighted_average = total_weighted_score / total_weight
    
    # تبدیل میانگین به کاراکتر
    if weighted_average >= 4:
        return 'A'
    elif weighted_average >= 3:
        return 'B'
    elif weighted_average >= 2:
        return 'C'
    elif weighted_average >= 1:
        return 'D'
    else:
        return 'F'

# ورودی
n = int(input("تعداد امتحانات: "))
exams = []

for _ in range(n):
    line = input().strip().split()
    weight = int(line[0])
    grade = line[1]
    exams.append((weight, grade))

# محاسبه و چاپ نمره نهایی
final_grade = calculate_grade(n, exams)
print(final_grade)
