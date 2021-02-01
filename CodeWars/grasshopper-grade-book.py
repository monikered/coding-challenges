# Complete the function so that it finds the mean of the three scores passed to it and returns the letter value associated with that grade.

grade_dict = {(0,60): 'F', (60,70): 'D', (70,80): 'C', (80,90): 'B', (90,100): 'A'}

def get_grade(*args):
    grade = ''
    for (a,b) in grade_dict:
        if sum(args)/3 <= b and sum(args)/3 >= a:
            grade = grade_dict[(a,b)]
    return grade
