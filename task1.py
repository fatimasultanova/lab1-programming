students = [
    {"name": "Aysel", "score": 87},
    {"name": "Anar", "score": 95},
    {"name": "Murad", "score": 62},
    {"name": "Leyla", "score": 45},
    {"name": "Konul", "score": 78},
    {"name": "Fatima", "score": 120}
]

passed_students = []

categories = {
    "Excellent": 0,
    "Good": 0,
    "Satisfactory": 0,
    "Failed": 0
}

for student in students:
    score = student["score"]
    
    if score < 0 or score > 100:
        continue
    
    if score >= 51:
        passed_students.append(student["name"])
    
    if 90 <= score <= 100:
        categories["Excellent"] += 1
    elif 70 <= score <= 89:
        categories["Good"] += 1
    elif 51 <= score <= 69:
        categories["Satisfactory"] += 1
    elif score < 51:
        categories["Failed"] += 1

print("Passed Students:", passed_students)
print("Categories Count:", categories)