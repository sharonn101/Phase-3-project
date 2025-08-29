from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, SessionLocal

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

    @classmethod
    def create(cls, name):
        session = SessionLocal()
        user = cls(name=name)
        session.add(user)
        session.commit()
        session.close()
        return user

    @classmethod
    def get_all(cls):
        session = SessionLocal()
        users = session.query(cls).all()
        session.close()
        return users

    @classmethod
    def find_by_id(cls, user_id):
        session = SessionLocal()
        user = session.query(cls).get(user_id)
        session.close()
        return user

    @classmethod
    def delete(cls, user_id):
        session = SessionLocal()
        user = session.query(cls).get(user_id)
        if user:
            session.delete(user)
            session.commit()
        session.close()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    status = Column(String, default="pending")
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")

    @classmethod
    def create(cls, title, user_id):
        session = SessionLocal()
        task = cls(title=title, user_id=user_id)
        session.add(task)
        session.commit()
        session.close()
        return task

    @classmethod
    def get_all(cls):
        session = SessionLocal()
        tasks = session.query(cls).all()
        session.close()
        return tasks

    @classmethod
    def find_by_id(cls, task_id):
        session = SessionLocal()
        task = session.query(cls).get(task_id)
        session.close()
        return task

    @classmethod
    def delete(cls, task_id):
        session = SessionLocal()
        task = session.query(cls).get(task_id)
        if task:
            session.delete(task)
            session.commit()
        session.close()
