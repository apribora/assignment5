import csv

all_students = []
with open('dataset.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        all_students.append(row)

#Крок 3
for student in all_students:
    avg_score = 0
    for score in student:
        if score in ['Основи програмування', 'Лінійна алгебра', 'Проекційна геометрія', 'Математичний аналіз']:
            avg_score += int(student[score])
    student["Середня оцінка"] = avg_score / 4

#4.1.
while True:
    target_group = input("Введіть назву ОДНІЄЇ групи для експорту: ")
    if target_group in set(all_students[group_name]['Група'] for group_name in range(len(all_students))):
        break
    else:
        print("Такої групи не існує, спрообуйте ще раз.")

