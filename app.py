from flask import Flask, render_template
from forms import *
from models import *



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

        # Check if username exists
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "Someone else has taken this username!"
        
        # Adding user to database
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "User created"


    return render_template("index.html", form=reg_form)


if __name__ == "__main__":
    app.run(debug=True)