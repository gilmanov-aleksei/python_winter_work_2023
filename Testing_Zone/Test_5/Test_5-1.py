#! /usr/bin/python

students = {
    1: {'name': 'Pete', 'age': 25, 'profession': 'developer'},
    0: {'name': 'Nick', 'age': 26, 'profession': 'tester'}
}

for d in students:
    print(d, students[d])
    for i in students[d]:
        print(i, students[d][i])
