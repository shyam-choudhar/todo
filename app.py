from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRSCK_MODIFICATION'] = False
db = SQLAlchemy(app)
class Project(db.Model):
      sno = db.Column(db.Integer,primary_key = True) 
      title = db.Column(db.String(200),nullable = False)
      dect = db.Column(db.String(200),nullable = False)
      date_created = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self) -> str:
      return f"{self.sno} - {self.title}"


@app.route('/')
def hello_world():
      return render_template('index.html')
       # return 'Hello, World_ !'
# @app.route("/")
# def home():
#     return render_template("index.html")
@app.route('/prodect')
def prodect():
       return 'prodect in here '
       
if __name__ == '__main__':
    app.run(debug=True,port = 5500)

    with app.app_context():  # ✅ Fix application context issue
        db.create_all()  # ✅ Now it runs inside the Flask app context
    app.run(debug=True, port=5500)

# import os
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     print("Current Directory:", os.getcwd())  # Print working directory
#     print("Template Folder Path:", app.template_folder)  # Debugging path
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True, port=5500)c:\Users\VICTUS\Desktop\app
