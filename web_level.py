
from flask import Flask, render_template

from db_level import UserManager

app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'


@app.route('/')
def users_list():

    users = UserManager().get_all()
    return render_template('users_list.html', users=users)


@app.route('/add/', )
def users_add():
    return 'ok'


@app.route('/edit/<user_id>/', )
def users_edit(user_id):
    return 'ok'


@app.route('/delete/<user_id>/', )
def users_delete(user_id):
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
