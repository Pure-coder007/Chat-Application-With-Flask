from flask import Flask, render_template
from forms import RegistrationForm, LoginForm  # Import the specific forms
from models import User, db
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.secret_key = 'replace later'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://my_chat_user:wyXp8PuPAnmL8wF27lvwBvDiNxEkqQeS@dpg-cless13l00ks739th3pg-a.oregon-postgres.render.com/my_chat'

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Hashed password
        hashed_password = pbkdf2_sha256.hash(password)

        # Adding user to database
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return "User created"
    return render_template("index.html", form=reg_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return"Logged in finally"

    return render_template("login.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True)
