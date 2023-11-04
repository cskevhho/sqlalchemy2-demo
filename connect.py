from sqlalchemy import create_engine, text

"""
This starts up the SQLAlchemy engine, we adjust the
passed in parameter to our database specifications,
echo is just to have it repeat to us what it had done.
Here I am just using SQLite as the DB and server because
it can be run in memory/saved onto a .db file.    
"""


engine = create_engine("sqlite:///sample.db", echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))
