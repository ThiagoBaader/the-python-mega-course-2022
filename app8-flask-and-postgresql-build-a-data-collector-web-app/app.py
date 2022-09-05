# library import
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)

# creating the PostGreSQL database model
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__= "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


# creating index page
@app.route("/")
def index():
    return render_template("index.html")


# creating success page
@app.route("/success", methods=['POST'])
def success():
    # capturing user input
    if request.method == 'POST':
        email_ = request.form["email_name"]
        height_ = request.form["height_name"]

        # storing user data to the database
        if db.session.query(Data).filter(Data.email == email_).count() == 0:
            data = Data(email_, height_)
            db.session.add(data)
            db.session.commit()

            # calculating data statistics
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height, 1)
            count = db.session.query(Data.height).count()

            # emailing database values back to user
            send_email(email_, height_, average_height, count)

            return render_template("success.html")
        return render_template("index.html", text="Seems we've got something from that email address already!")


if __name__ == '__main__':
    app.debug = True
    app.run()
