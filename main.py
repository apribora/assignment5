import csv

all_students = []
with open('dataset.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        all_students.append(row)

#3
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

#4.2.
fieldnames = ['Id', 'Прізвище', 'Ім\'я', 'Група',
              'Основи програмування', 'Лінійна алгебра',
              'Проекційна геометрія', 'Математичний аналіз',
              'Середня оцінка']
#4.2/3
with open(f"{target_group}.txt", mode='w', encoding='utf-8', newline='') as file:
    # 4.4.
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # 4.5.
    writer.writeheader()

    # 4.6.
    for student in all_students:
        if student["Група"] == target_group:
            writer.writerow(student)

print(f"Завершено. Створено файл {target_group}.")