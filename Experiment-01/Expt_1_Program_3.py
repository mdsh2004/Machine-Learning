def sort_students_by_score(students):
   # Sort the list of tuples using sorted()
   sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
   return sorted_students
   # Example usage:
students = [
("Mohammed Shaikh", 98),
("Virat", 90),
("Hardik", 88),
("Bhumrah", 93),
("Sky", 75)
]
sorted_students = sort_students_by_score(students)
print("Sorted students:", sorted_students)
print("UIN : 211P017")