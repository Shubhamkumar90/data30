students={
    "Tom":50,
    "Jerry":70,
    "Bob":100
}
top=max(students,key=students.get)
print(f"Name: {top}\nMarks: {students[top]}")