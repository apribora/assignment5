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

while True:
    target_group = input("Введіть назву ОДНІЄЇ групи для експорту: ")
    if target_group in set(all_students[group_name]['Група'] for group_name in range(len(all_students))):

        print("poka rabotaet")

        break
    else:
        print("Такої групи не існує, спрообуйте ще раз.")

request = input("Введіть назву однієї групи для експорту: ")
while request not in set(all_students[i]['Група'] for i in range(len(all_students))):
    request = input("Введіть дійсну назву групи для експорту: ")
