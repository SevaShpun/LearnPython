from app import db
from tools.modeles import Answers, Tasks, TaskRequest


def get_main_tasks() -> list[dict]:
    """Получить актуальные задания"""
    tasks = Tasks.query.filter_by(status=1).all()
    return [i.get_json() for i in tasks]


def get_archive_tasks() -> list[dict]:
    """Получить задания из архива"""
    tasks = Tasks.query.filter_by(status=2).all()
    return [i.get_json() for i in tasks]


def add_new_answer(first_name: str, last_name: str, answer: str, task_id: int) -> Answers:
    """Добавить новый ответ"""
    answer = Answers(first_name, last_name, answer, task_id)
    db.session.add(answer)
    db.session.commit()
    return answer


def add_new_task_request(title: str, description: str, start_code: str, comment: str) -> TaskRequest:
    """Новый запрос на задание"""
    task = TaskRequest(title, description, start_code, comment)
    db.session.add(task)
    db.session.commit()
    return task


def get_answer_by_id(answer_id: int) -> dict:
    """Получить ответ по id"""
    answer: Answers = Answers.query.filter_by(id=answer_id).first()
    return answer.get_json() if answer else {'id': 0, 'task_id': 0, 'first_name': "Имя",
                'last_name': "Фамилия", 'answer': "Лучшего ответа пока нет"}


if __name__ == "__main__":
    db.create_all()

