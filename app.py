from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

with app.app_context():
    db.create_all()

# Check if the users already exist to avoid duplicate inserts
    if not User.query.first():
        # Adding sample users
        user1 = User(username='JohnDoe', password='password123', points=100)
        user2 = User(username='JaneSmith', password='password456', points=200)
        user3 = User(username='Alice', password='password789', points=300)
        
        # Add users to session and commit to the database
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.commit()
    
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return render_template('home.html', user=user)
        else:
            return 'Invalid username or password'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)