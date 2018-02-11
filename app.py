from flask import Flask, render_template
import os
import pymysql

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

basedir = os.path.abspath(os.path.dirname(__file__))

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/test?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()

        for i in range(count):
            u = User(username=forgery_py.name.full_name(),
                     email=forgery_py.email.address(),
                     password=forgery_py.basic.password())

            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

        return

users = User.query.all()

@app.route('/')
def home_page():
    return render_template("index.html", users=users)

@app.route('/about')
def about_page():
    title = "about"
    return render_template("about.html", title=title)

@app.route('/review')
def review_page():
    title = "review"
    return render_template("review.html", title=title)

@app.route('/contact')
def contact_page():
    title = "contact"
    return render_template("contact.html", title=title)

@app.route('/tlds/<domain_name>')
def domain_extension(domain_name):
    return render_template("tld_base.html", domain_name=domain_name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.secret_key = 'here-you-are'
if __name__ == '__main__':
    app.run(debug=True)
