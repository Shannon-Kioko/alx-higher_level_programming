## 0x0F. Python - Object-relational mapping
Resources
Read or watch:

[Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
[mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/) (please don’t pay attention to _mysql)
[MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
[SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
[SQLAlchemy]
[mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
[Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
[Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
[10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
[Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
[SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers) (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
[SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
[Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer)

###  0-select_states.py
Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported

### 1-filter_states.py
