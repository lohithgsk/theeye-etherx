from flask import *


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = "KrrrzPPghtfgSKbtJEQCTA"


@app.route('/')
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html')
    else:
        return render_template('dashboard.html')

@app.route('/theme')
def theme():
    if request.method == 'GET':
        return render_template('theme.html')
    else:
        return render_template('theme.html')
