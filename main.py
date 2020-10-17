from flask import Flask, render_template
from flask import request
from country_list import countries_for_language

app = Flask(__name__)



@app.route('/login', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pswd"]
        if not email:
            message = 'Please fill out this field.'
            return render_template('login.html', message=message)
        if not password:
            return render_template('login.html', message_p='Please fill out this field.')
        return render_template('login.html', message_success="Successful login!!")

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    countries = dict(countries_for_language('en'))
    if request.method == "POST":
        req = request.form
        missing = []
        for field, input in req.items():
            if input == "":
                missing.append(field)

        if missing:
            feedback = " {}".format(', '.join(missing))
            return render_template('signup.html', countries=countries,
                                   feedback=feedback)
        if req["Email"] != req["Confirm email"]:
            return render_template('signup.html', countries=countries,
                                   email_match="Emails don't match")
    return render_template('signup.html', countries=countries)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
