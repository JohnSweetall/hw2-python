# Author: John Sweetall jts6052@psu.edu

def getGradePoint(grade):

  if (grade == "A"):
    return 4.0
  elif (grade == "A-"):
    return 3.67
  elif (grade == "B+"):
    return 3.33
  elif (grade == "B"):
    return 3.0
  elif (grade == "B-"):
    return 2.67
  elif (grade == "C+"):
    return 2.33
  elif (grade == "C"):
    return 2.0
  elif (grade == "D"):
    return 1.0
  elif (grade == "F"):
    return 0.0
  else:
    return 0.0

def run ():
  gradepoint1 = input("Enter your course 1 letter grade: ")
  grade1 = getGradePoint(gradepoint1)
  credit1 = float(input("Enter course 1 credit: "))
  print(f"Grade point for course 1 is: {grade1}")

  gradepoint2 = input("Enter your course 2 letter grade: ")
  grade2 = getGradePoint(gradepoint2)
  credit2 = float(input("Enter course 2 credit: "))
  print(f"Grade point for course 2 is: {grade2}")

  gradepoint3 = input("Enter your course 3 letter grade: ")
  grade3 = getGradePoint(gradepoint3)
  credit3 = float(input("Enter course 3 credit: "))
  print(f"Grade point for course 3 is: {grade3}")

  GPA = (grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / (credit1 + credit2 + credit3)

  print(f"Your GPA is: {GPA}")





  




