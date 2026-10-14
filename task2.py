from functools import reduce

students = [
    {"name": "Aysel", "score": 87},
    {"name": "Anar", "score": 95},
    {"name": "Murad", "score": 62},
    {"name": "Leyla", "score": 45},
    {"name": "Konul", "score": 78},
    {"name": "Fatima", "score": 120}
]

valid_passed = list(filter(lambda s: 51 <= s["score"] <= 100, students))

formatted_strings = list(map(lambda s: f"{s['name']}: {s['score']}", valid_passed))

total_score = reduce(lambda acc, s: acc + s["score"], valid_passed, 0)
average_score = total_score / len(valid_passed) if valid_passed else 0

print("Formatted Passed Students:", formatted_strings)
print("Average Score of Passed Students:", average_score)