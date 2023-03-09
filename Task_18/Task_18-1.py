#! /usr/bin/python

# Задача 18 (НЕ ЗАКОНЧЕНА)
# Разработать систему учета решения задач учениками курса «Разработчик на Питоне».
# Проблема. Преподаватель каждый урок задает некоторое количество задач
# в качестве домашнего задания, для упрощения можно считать, что одну.
# Каждый ученик решает каждую задачу. Переводит ее статус в решенную.
# Преподаватель проверяет каждую задачу каждого ученика и либо подтверждает ее
# статус как решенную или меняет ее статус как не решенную.
# Вопрос. Как спроектировать систему классов на Питоне для решения задачи учета.
# Разработайте систему классов (Teacher, Pupil, Lesson, Task. Нужен ли класс Группа)
# Разработайте систему атрибутов для каждого состояния каждого объекта.
# Разработайте систему методов для каждого объекта.
# Отчетность? Запросы? Начните с формулировки решаемой задачи спецификации
# или технического задания. Затем спроектируйте классы, атрибуты, методы.
# Протестируйте систему.


import openpyxl

class Teacher:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)
    def delete_lesson(self, lesson):
        self.lessons.remove(lesson)

    def view_lessons(self):
        for lesson in self.lessons:
            print(f"Урок {lesson.lesson_number}")

    def view_lesson(self, lesson_number):
        for lesson in self.lessons:
            if lesson.lesson_number == lesson_number:
                return lesson
        print("Урок не найден")
        return None
    def check_pupil_task(self, pupil, lesson_num, task_num, status):
        pupil.results[lesson_num][task_num] = status

    def change_task_status(self, lesson_num, task_num, status):
        for lesson in self.lessons:
            if lesson.num == lesson_num:
                lesson.tasks[task_num-1]['status'] = status


class Pupil:
    def __init__(self, name):
        self.name = name
        self.results = {}

    def solve_task(self, lesson_num, task_num):
        self.results[lesson_num][task_num] = False

    def change_task_status(self, lesson_num, task_num, status):
        self.results[lesson_num][task_num] = status


class Lesson:
    def __init__(self, num):
        self.num = num
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'num': len(self.tasks)+1, 'description': task, 'status': None})

    def get_tasks_list(self):
        return [task['description'] for task in self.tasks]


class ExcelFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.data = {}

    def load_data(self):
        self.workbook = openpyxl.load_workbook(self.file_name)
        self.sheet = self.workbook.active

        for row in range(2, self.sheet.max_row+1):
            pupil_name = self.sheet.cell(row=row, column=1).value
            lesson_num = self.sheet.cell(row=1, column=row).value
            tasks = {}

            for task in range(1, 4):
                task_status = self.sheet.cell(row=row, column=task+1).value
                if task_status is None:
                    tasks[task] = None
                else:
                    tasks[task] = bool(task_status)

while True:
    user_input = int(input("Введите число: 1 - Учитель, 2 - Ученик, "
                           "3 - Загрузить из файла, 4 - Сохранить в файл, 0 - Выход: "))
    if user_input == 1:
        Teacher.view_lessons()
        teacher_input = int(input("Введите число: 1 - посмотреть уроки, 2 - посмотреть урок по номеру, "
                  "3 - добавить урок, 4 - удалить урок, 0 - вернуться в меню: "))
        if teacher_input == 1:
            Teacher.view_lessons()
        elif teacher_input == 2:
            lesson_number = int(
                input("Введите номер урока для просмотра: ")
            )
            lesson = Teacher.view_lesson(lesson_number)
            if lesson:
                lesson.view_tasks()
        elif teacher_input == 3:
            lesson_number = int(
                input("Введите номер урока чтобы добавить: ")
            )
            lesson = Lesson(lesson_number)
            Teacher.add_lesson(lesson)
        elif teacher_input == 4:
            lesson_number = int(
                input("Введите номер урока для удаления: ")
            )
            lesson = Teacher.view_lesson(lesson_number)
            if lesson:
                Teacher.delete_lesson(lesson)
    elif user_input == 2:
        print("Ученик")
        # pupil_input = int(input("Введите число: 1 - для просмотра заданий, 2 - для просмотра задания по номеру, "
        #           "3 - добавить задание, 4 - удалить задание, 0 - вернуться в меню: "))
        # if pupil_input == 1:
        #     Pupil.view_tasks()
        # elif pupil_input == 2:
        #     task_number = int(
        #         input("Введите номер задания для просмотра: ")
        #     )
        #     task = Pupil.view_task(task_number)
        #     if task:
        #         print(f"Задание {task.number}: {task.description}, {task.status}")
        # elif pupil_input == 3:
        #     task_number = int(
        #         input("Введит номер для добавления задания: ")
        #     )
        #     task_description = input("Введите номер задания для просмотра: ")
        #     task = Lesson.task(task_number, task_description)
        #     Pupil.add_task(task)
        # elif pupil_input == 4:
        #     task_number = int(
        #         input("Введите номер задания для удаления: ")
        #     )
        #     task = Pupil.view_task(task_number)
        #     if task:
        #         Pupil.delete_task(task)
    elif user_input == 3:
        print("Загрузить из файла")
    elif user_input == 4:
        print("Сохранить в файл")
    elif user_input == 0:
        break
