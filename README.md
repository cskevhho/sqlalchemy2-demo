# SQLAlchemy 2.0 Practice

## Some words

So there kind of is an order to view the files just so that the storytelling of what I am trying to convey to you guys is a bit more clear.

This is structured using User and Comment as our models (i.e in fashion of like Facebook, YouTube).
This repo shows a rough idea of how this all looks using SQLAlchemy to program any CRUD logic with an RDBMS.

**NOTE, THIS IS NOT DESIGNED WITH FLASK IN MIND**, but it should not be difficult to transition into.

**NOTE2, main.py has one job (in this repo) and it's just so that we don't have to type it in ***every*** file we've created (yes it's that important)**  

Original content by Ssali Jona :D cheers!

## Recommended order to view files

    1. connect.py (note main.py has the session engine line)
    2. models.py
    3. create_tables.py
    4. persistence.py
    5. session_select.py
    6. session_select_one.py
    7. join_select.py
    8. session_update.py
    9. session_delete.py