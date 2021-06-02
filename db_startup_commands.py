import os

# only run this the very first time you start the site.
# afterwards only run app.py

if __name__ == '__main__':
    os.system('set FLASK_APP=app.py')  # use set for Windows or export for Linux
    os.system('flask db init')
    os.system('flask db migrate -m "intializing database"')
    os.system('flask db upgrade')
    os.system('python -m flask run')
