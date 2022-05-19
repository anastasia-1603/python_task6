from flask import Flask, render_template, request, url_for, redirect
import logic

app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def start_page():
    if 'month' in request.form:
        month = int(request.form["month"])
    else:
        month = logic.get_curr_month()
    if 'year' in request.form:
        year = int(request.form["year"])
    else:
        year = logic.get_curr_year()
    if 'day' in request.form:
        day = int(request.form["day"])
    else:
        day = logic.get_curr_day()
    days_list = logic.get_days_list(year, month)
    return render_template('not_logged_in.html', day=day, month=month, year=year, days_list=days_list,
                           curr_year=logic.get_curr_year())


@app.route('/',  methods=['GET', 'POST'])
def select_month():
    year = int(request.form["year"])
    day = int(request.form["day"])
    month = int(request.form.get('month'))
    days_list = logic.get_days_list(year, month)
    return render_template('not_logged_in.html', day=day, month=month, year=year, days_list=days_list,
                           curr_year=logic.get_curr_year())


if __name__ == "__main__":
    app.run(debug=True)
