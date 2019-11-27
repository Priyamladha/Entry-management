from flask import Flask, render_template, request, jsonify


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(20))
    email = db.Column(db.String(120))
    number = db.Column(db.String(20),primary_key=True)
    checkin = db.Column(db.String(20))
    checkout = db.Column(db.String(20),nullable=True)
    hostname = db.Column(db.String(20),nullable=True)
    def __repr__(self):
        return f"User('{self.name}','{self.email}','{self.number}','{self.checkin}','{self.checkout}')"

class Host(db.Model):
    name = db.Column(db.String(20))
    email = db.Column(db.String(120))
    number = db.Column(db.String(20),primary_key=True)
    def __repr__(self):
        return f"Host('{self.name}','{self.email}','{self.number}')"
db.create_all()


@app.route('/')
def download_file():
    return render_template('index.html')

@app.route('/host')
def download():
    return render_template('host.html')

@app.route('/', methods=['POST'])
def user_post():

    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    value = request.form['check']
    if value=="checkin":
        import checkin
        flagg=checkin.send(name,email,number)
        return render_template("index.html",flagg=flagg)
    else:
        import checkout
        flag = checkout.send(name,email,number)
        return render_template("index.html",flag=flag)


@app.route('/host', methods=['POST'])
def host_post(): 
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    import create_host
    create_host.create(name,email,number)
    return render_template("host.html")

if __name__ == "__main__":
    app.run(debug=True)