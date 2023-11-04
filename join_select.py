from main import session
from models import User, Comment
from sqlalchemy import select

"""
A much more cleaned up "statement", we can see how
similar it is to SQL, just minus the SQL statements
and more actual programming-y things. 
"""

stmnt = (
    select(Comment)
    .join(Comment.user)
    .where(User.username == "john")
    .where(Comment.text == "Hello World")
)

# This returns the repr function we defined in whatever we are searching
result = session.scalars(stmnt).one()

# session.scalars(stmnt).one().text would return just Hello World
print(result)
