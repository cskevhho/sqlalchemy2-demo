from main import session
from models import User, Comment


result = session.query(User).filter_by(username="jane").first()

"""
This prints out the column title and value of the column
note just change username to any other attribute we've set
works same way [Note: Not a single query to be seen yet.]
"""

print(result)