from flask import Flask, render_template, Response, request, render_template_string
app = Flask(__name__)


# главная страница
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


# запуск обработки документов
@app.route('/start')
def start():
    # if # здесь ваш код обработки документов
        return render_template("start.html", start_data='Обработка завершена. Посмотреть <a href="/output_data">результаты.</a>')
 # условие, если файлы не загружены:
 #   else:
 #    return render_template_string('<h2 align="center">Не загружены файлы для обработки. Вернитеcь на <a href="/index">главную страницу.</a></h2>')

# вывод результатов
@app.route('/output_data')
def output():
    # if # здесь ваш код вывода результатов
    # else:
# условие, если запуск не был произведен, и пользователь пытается попасть на # страницу с результатами:
        return render_template_string('<h2 align="center">Для начала надо нажать на "Запуск". Вернитеcь на <a href="/index">главную страницу.</a></h2>')

# запуск Flask-приложения:
if __name__ == "__main__":
    app.run(debug=False)