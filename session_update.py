from main import session
from models import User, Comment

# Change the first comment we find (primary key == 1 below)
comment = session.query(Comment).filter_by(id=1).first()

comment.text = "This should replace Hello World"

session.commit()  # yes, that's it. if you saw COMMIT in the log, the transaction was successsful

# you can test this out, try python3 join_select.py now, it shouldn't work.