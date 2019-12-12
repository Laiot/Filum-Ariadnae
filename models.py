from database import Base
from flask_security import UserMixin, RoleMixin
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                       String, ForeignKey

class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))

class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))

class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))

class Keys(Base):
    __tablename__ = 'keys'
    id = Column(Integer, primary_key=True)
    token = Column(String(255))
    description = Column(String(500))
    expiration=Column(DateTime)
    urledu=Column(String(500))
    urlsurvey=Column(String(500))

class Survey(Base):
    __tablename__ = 'survey'
    id = Column(Integer, primary_key=True)
    sessionid=Column(String(255))
    classCode = Column(String(100))
    type = Column(String(100))
    path = Column(String(255))
    history = Column(String(100))
    gender = Column(String(1))
    age=Column(Integer)
    residence = Column(String(20))
    q1=Column(String(1))
    q2=Column(String(1))
    q3=Column(String(1))
    q4=Column(String(1))
    q5=Column(String(1))
    q6=Column(String(1))
    q7=Column(String(1))
    q8 = Column(String(1))
    q9 = Column(String(1))
    freetext = Column(String(2000))

    def __init__(self, sessionid=None,classCode=None, type=None, path=None,history=None,gender=None,age=None,residence=None,q1=None,q2=None,q3=None,q4=None,q5=None,q6=None,q7=None,q8=None,q9=None,freetext=None):
        self.sessionid = sessionid
        self.classCode=classCode
        self.type=type
        self.path = path
        self.history = history
        self.gender = gender
        self.age = age
        self.residence = residence
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.freetext = freetext
