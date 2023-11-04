from models import Base, User, Comment
from connect import engine

"""
So this file is just really here to generate the tables
via the `create_all()` function call found in SQLAlchemy's
DeclarativeBase class object (lots of definitions
and attributes)
"""


print("CREATING TABLES:")
Base.metadata.create_all(bind=engine)