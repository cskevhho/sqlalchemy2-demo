from models import User, Comment
from main import session

"""
This file contains a set of User objects,
using this file as a means of showing how
how the insert works in SQLAlchemy, if you
run this as `python3 persistence.py` (but
first you have to run `python3 create_tables.py`)
the terminal will display the SQL commands that are
being made for us (we are not directly creating the
statements in SQLAlchemy, this is good for us since
we will not be making complex queries and protects us
from injection attacks)
"""


user1 = User(
    username="john",
    email_address="john.doe@john.doe",
    comments=[Comment(text="Hello World"), Comment(text="Test 123")],
)

jane = User(
    username="jane",
    email_address="jane.doe@jane.doe",
    comments=[Comment(text="Please god"), Comment(text="Please work")],
)

joon = User(
    username="joon",
    email_address="joon.kim@joon.kim",
)

session.add_all([user1, jane, joon])

session.commit()
