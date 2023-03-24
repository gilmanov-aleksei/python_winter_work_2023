#! /usr/bin/python


# def func(f):
#     return f
#
#
# def hello():
#     print('Привет!!!')
#
#
# hello()
# func(hello)()

# def speak(text):
#     def whisper(t):
#         return t.lower() + '...'
#
#     return whisper(text)
#
#
# print(speak('Hello, World'))

# def speak():
#     def whisper(t):
#         return t.lower() + '...'
#
#     return whisper
#
#
# # Получаем из функции speak объект функции whisper
# wr = speak()
# # Вызываем функцию с одним аргументом
# print(wr('Hello, World'))

def speak(text):
    def whisper():
        print(text.lower() + '...')

    return whisper


foo = speak('Hello World')
bar = speak('Wellcome')

foo()
bar()
