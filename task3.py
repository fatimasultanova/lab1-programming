import copy

students = [
    {"name": "Aysel", "score": 87},
    {"name": "Anar", "score": 95},
    {"name": "Murad", "score": 62},
    {"name": "Leyla", "score": 45},
    {"name": "Konul", "score": 78},
    {"name": "Fatima", "score": 120}
]

def apply_to_scores(students_list, callback):
    new_list = copy.deepcopy(students_list)
    for student in new_list:
        student["score"] = callback(student["score"])
    return new_list

def add_bonus(score):
    return min(100, score + 5)

students_with_bonus = apply_to_scores(students, add_bonus)

students_scaled = apply_to_scores(students, lambda score: round(score / 10, 1))

print("Original Students:", students)
print("Students with Bonus:", students_with_bonus)
print("Students with 0-10 Scale:", students_scaled)