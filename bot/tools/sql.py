from sqlalchemy import create_engine, Integer, Column, VARCHAR, Table, select, update
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from tools.modeles import Answers, Tasks, Base
from config import sql_login


engine = create_engine(sql_login)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def reconnect(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            try:
                session.rollback()
                return func(*args, **kwargs)
            except Exception as ex:
                print(ex)
    return wrapper


@reconnect
def add_new_task(title, task, start=''):
    """Добавляем новый таск"""
    session.add(Tasks(title, task, start))
    session.commit()
    return True


@reconnect
def update_visibility(task_id, vis):
    """Изменяем видимость"""
    u = update(Tasks).where(Tasks.id == task_id).values(status=vis). \
        execution_options(synchronize_session="fetch")
    session.execute(u)
    session.commit()


@reconnect
def get_tasks_by_id(task_id) -> list[Answers]:
    """Получаем массив ответов"""
    session.commit()
    return session.query(Answers).filter_by(task_id=task_id).all()


@reconnect
def update_best_answer(answer_id):
    """Изменяем видимость"""
    task_id = session.query(Answers).filter_by(id=answer_id).first().task_id
    u = update(Tasks).where(Tasks.id == task_id).values(answer_id=answer_id). \
        execution_options(synchronize_session="fetch")
    session.execute(u)
    session.commit()
