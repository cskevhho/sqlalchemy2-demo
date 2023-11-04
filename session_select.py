from main import session
from models import User, Comment
from sqlalchemy import select

"""
A simple example of how a select all statement would work.
"""

users = session.query(User).all()

for u in users:
    print(u)