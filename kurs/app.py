import os

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_admin.contrib.sqla.fields import QuerySelectField, QuerySelectMultipleField
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(20)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
app.config['BABEL_DEFAULT_LOCALE'] = 'ru'

db = SQLAlchemy(app)


# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	role = db.Column(db.String(100), nullable=False)
# 	username = db.Column(db.String(80), unique=True, nullable=False)
# 	email = db.Column(db.String(120), unique=True, nullable=False)
# 	password = db.Column(db.String(), nullable=False)
#
# 	def __str__(self):
# 		return f'{self.username}'


class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	description = db.Column(db.Text)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'))
	solved_by_teacher = db.Column(db.Boolean, default=False)
	solved_by_student = db.Column(db.Boolean, default=False)
	completed = db.Column(db.Boolean, default=False)
	
	def __str__(self):
		return f'{self.name}'


class Lesson(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	description = db.Column(db.Text)
	tasks = db.relationship('Task', backref='lesson', lazy='dynamic')
	
	def __str__(self):
		return f'{self.name}'


class LessonForm(FlaskForm):
	name = StringField('Название урока', validators=[DataRequired()])
	description = TextAreaField('Описание урока', validators=[DataRequired()])
	tasks = QuerySelectMultipleField('Задачи', query_factory=lambda: Task.query.all(), allow_blank=True)
	submit = SubmitField('Создать')


class TaskForm(FlaskForm):
	name = StringField('Название задачи', validators=[DataRequired()])
	description = TextAreaField('Описание', validators=[DataRequired()])
	lesson = QuerySelectField('Урок', query_factory=lambda: Lesson.query.all(), allow_blank=True)
	submit = SubmitField('Создать')


class DeleteTaskForm(FlaskForm):
	task = QuerySelectField('Задача', query_factory=lambda: Task.query.all(), allow_blank=True)


class DeleteLessonForm(FlaskForm):
	lesson = QuerySelectField('Урок', query_factory=lambda: Lesson.query.all(), allow_blank=True)


@app.route('/')
def index():
	lessons = Lesson.query.all()
	task_count = len(Task.query.all())
	return render_template('index.html', lessons=lessons, task_count=task_count)


@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/lessons/<int:lesson_id>/tasks', methods=['GET', 'POST'])
def tasks(lesson_id):
	form = TaskForm()
	if form.validate_on_submit():
		task = Task(name=form.name.data, description=form.description.data, lesson_id=lesson_id)
		db.session.add(task)
		db.session.commit()
		return redirect(url_for('tasks', lesson_id=lesson_id))
	tasks = Task.query.filter_by(lesson_id=lesson_id).all()
	return render_template('tasks.html', tasks=tasks, form=form, lesson_id=lesson_id)


@app.route('/tasks/new', methods=['GET', 'POST'])
def new_task():
	form = TaskForm()
	if form.validate_on_submit():
		task = Task(name=form.name.data, description=form.description.data)
		db.session.add(task)
		db.session.commit()
		flash('Задача была создана!', 'success')
		return redirect(url_for('index'))
	return render_template('new_task.html', form=form)


@app.route('/lessons/<int:lesson_id>/tasks')
def tasks_by_lesson(lesson_id):
	lesson = Lesson.query.get_or_404(lesson_id)
	tasks = lesson.tasks.order_by(Task.created_at.desc()).all()
	return render_template('tasks.html', tasks=tasks, lesson=lesson)


@app.route('/tasks/solved_by_teacher/<int:id>')
def task_solved_by_teacher(id):
	task = Task.query.get_or_404(id)
	if task.solved_by_teacher:
		task.solved_by_teacher = False
	else:
		task.solved_by_teacher = True
	db.session.commit()
	return redirect(url_for('index'))


@app.route('/tasks/solved_by_student/<int:id>')
def task_solved_by_student(id):
	task = Task.query.get_or_404(id)
	if task.solved_by_student:
		task.solved_by_student = False
	else:
		task.solved_by_student = True
	db.session.commit()
	return redirect(url_for('index'))


@app.route('/tasks/delete', methods=['GET', 'POST'])
def delete_task():
	form = DeleteTaskForm()
	if form.validate_on_submit():
		task = form.task.data
		db.session.delete(task)
		db.session.commit()
		flash('Задача была удалена!', 'success')
		return redirect(url_for('index'))
	return render_template('delete_task.html', form=form)


@app.route('/lesson/new', methods=['GET', 'POST'])
def new_lesson():
	form = LessonForm()
	if form.validate_on_submit():
		# process the form data
		lesson = Lesson(name=form.name.data, description=form.description.data)
		db.session.add(lesson)
		db.session.commit()
		flash('Урок был создан!', 'success')
		return redirect(url_for('index'))
	
	return render_template('new_lesson.html', title='New Lesson', form=form)


@app.route('/lesson')
def lesson():
	lesson_id = request.args.get('lesson_id', None)
	if lesson_id is not None:
		lesson = Lesson.query.filter_by(id=lesson_id).first()
		if lesson is not None:
			tasks = Task.query.all()
			return render_template('lesson.html', title=lesson.name, lesson=lesson, tasks=tasks)
	return redirect(url_for('lesson'))


@app.route('/lesson/delete', methods=['GET', 'POST'])
def delete_lesson():
	form = DeleteLessonForm()
	if form.validate_on_submit():
		lesson = form.lesson.data
		db.session.delete(lesson)
		db.session.commit()
		flash('Урок был удален!', 'success')
		return redirect(url_for('index'))
	return render_template('delete_lesson.html', form=form)


if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run(debug=True)
