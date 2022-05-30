from flask import Flask, render_template, request, url_for, redirect, g
import logic
import os
import sqlite3
from FDataBase import FDataBase


DATABASE = '/tmp/calendar.db'
DEBUG = True
SECRET_KEY = ''

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, "calendar.db")))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/',  methods=['GET', 'POST'])
def start_page():
    db = get_db()
    dbase = FDataBase(db)
    req = request
    # if request.method == 'POST':
    #     print(request.form.get('day'))
    #     dbase.addEvent(request.form.get('day'), request.form.get('month'), request.form.get('year'), "текст")

    if 'year' in request.args or 'month' in request.args or 'day' in request.args:
        year = int(request.args['year'])
        month = int(request.args['month'])
        day = int(request.args['day'])
    else:
        month = logic.get_curr_month()
        year = logic.get_curr_year()
        day = logic.get_curr_day()

    days_list = logic.get_days_list(year, month)
    return render_template('calendar.html', day=day, month=month, year=year, days_list=days_list,
                           curr_year=logic.get_curr_year(), events=dbase.getEvents(day, month, year))


def add_event():
    db = get_db()
    dbase = FDataBase(db)
    if 'year' in request.args or 'month' in request.args or 'day' in request.args:
        dbase.addEvent(request.args['day'], request.args['month'], request.args['year'], "текст")
    return redirect(url_for('start_page'))


if __name__ == "__main__":
    app.run(debug=True)
