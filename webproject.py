from flask import Flask, render_template, request
from pymongo import MongoClient
client = MongoClient('127.0.0.1:27017')
db=client.student_data

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/news')
def news():
    return render_template("news.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def contact_post():
    print(request.form)
    data={}
    data['name'] = request.form['name']
    data['age'] = request.form['age']
    data['class'] = request.form['class']
    db.student.insert_one(data)
    #processed_text = {"name": name, "age": age, "class": std_class}
    return render_template("contact.html")

@app.route("/list",methods=['GET'])
def login():
    students=db.student.find()
    students=list(students)
    return render_template('list.html',students=students)

if __name__ == "__main__":
    app.run(debug=True)
