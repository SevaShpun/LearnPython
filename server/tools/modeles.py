from app import db
from datetime import datetime


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.VARCHAR(40), nullable=False)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    answer_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    start = db.Column(db.Text, nullable=False)

    def __init__(self, title: str, description: str, start: str):
        self.date = datetime.today().strftime("%d.%m.%Y")
        self.answer_id = 0
        self.status = 1
        self.title = title
        self.description = description
        self.start = start

    def __repr__(self):
        return '<Tasks(id: %s, title: %s, description: %s)>' % (self.id, self.title, self.description)

    def get_json(self) -> dict:
        """Возвращает все данные в виде словаря"""
        return {'id': self.id, 'date': self.date, 'title': self.title, 'description': self.description,
                'answer_id': self.answer_id, 'status': self.status, 'start': self.start}


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.VARCHAR(20), nullable=False)
    last_name = db.Column(db.VARCHAR(20), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __init__(self, first_name: str, last_name: str, answer: str, task_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.answer = answer
        self.task_id = task_id

    def __repr__(self):
        return '<Answers(id: %s, first_name: %s, task_id: %s)>' % (self.id, self.first_name, self.task_id)

    def get_json(self) -> dict:
        """Возвращает все данные в виде словаря"""
        return {'id': self.id, 'task_id': self.task_id, 'first_name': self.first_name,
                'last_name': self.last_name, 'answer': self.answer}


class TaskRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    start = db.Column(db.Text, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __init__(self, title: str, description: str, start: str, comment: str):
        self.status = 1
        self.title = title
        self.description = description
        self.start = start
        self.comment = comment

    def __repr__(self):
        return '<RequestTask(id: %s, title: %s, description: %s)>' % (self.id, self.title, self.description)
