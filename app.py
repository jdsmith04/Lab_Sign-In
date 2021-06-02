from flask import Flask, render_template, redirect, flash, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
from forms import SignInForm
import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # TODO: Find better secret key
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data.sqlite")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class StudentList(Table):
    student = Col('student')


class SignInOut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.Text)
    class_usage = db.Column(db.Integer)
    sign_in = db.Column(db.DateTime)
    sign_out = db.Column(db.DateTime)

    def __init__(self, student, class_usage, sign_in, sign_out):
        self.student = student
        self.class_usage = class_usage
        self.sign_in = sign_in
        self.sign_out = sign_out


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignInForm()
    if form.validate_on_submit():

        name = form.name.data.lower()
        class_usage = form.class_usage.data
        punch = datetime.datetime.now()
        # the epoch date is a place holder
        sign_out = datetime.datetime(1970, 1, 1, 0, 0, 0, 0)

        # finds particular student who hasn't signed out
        this_student = db.session.query(SignInOut) \
            .filter(SignInOut.student == name) \
            .order_by(SignInOut.id.desc()).first()

        # for signing in
        # 1st condition: is the db empty?
        # 2nd condition: does the student exist?
        # 3rd condition: the student has come back again
        if db.session.query(SignInOut).first() is None or this_student is None \
                or this_student.sign_out > this_student.sign_in:
            db.session.add(SignInOut(student=name, class_usage=class_usage,
                                     sign_in=punch, sign_out=sign_out))
            flash('You have successfully signed in')
        # for signing out
        else:
            this_student.sign_out = punch
            db.session.add(this_student)
            flash('You have successfully signed out')

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('signin.html', form=form)


@app.route('/occupants')
def occupants():
    occupying_students = db.session.query(SignInOut) \
        .filter(SignInOut.sign_out == datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).all()
    number_of_students = db.session.query(SignInOut) \
        .filter(SignInOut.sign_out == datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).count()
    flash(number_of_students)
    table = StudentList(occupying_students)

    return render_template('occupants.html', table=table, number_of_students=number_of_students)


@app.route('/utilization')
def utilization():
    
    return render_template('utilization.html')


if __name__ == '__main__':
    app.run()
