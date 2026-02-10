import csv

students = []
subjects = set()

with open('students.csv','r') as file:
    reader= csv.DictReader(file)


    for row in reader:
        student = {
            "name": row["name"],
            "marks": {
                "math": int(row["math"]),
                "science": int(row["science"]),
                "english": int(row["english"])
            }
        }
        students.append(student)
        subjects.update(student["marks"].keys())
