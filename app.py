from flask import Flask, render_template, request
import logic

app = Flask(__name__)


@app.route('/')
def start_page():
    month = logic.get_curr_month()
    year = logic.get_curr_year()
    days_list = logic.get_days_list(year, month)
    month_name = logic.month_num_to_name(month, "en")
    return render_template('not_logged_in.html', month=month_name, year=year,
                           days_list=days_list, curr_year=year)


@app.route('/<int:year>/<int:month>')
def month_calendar(year, month):
    days_list = logic.get_days_list(year, month)
    month_name = logic.month_num_to_name(month, "en")
    return render_template('not_logged_in.html', month=month_name, year=year,
                           days_list=days_list, curr_year=year)


@app.route('/<int:year>/<int:month>/<int:day>')
def day_calendar(year, month, day):
    days_list = logic.get_days_list(year, month)
    month_name = logic.month_num_to_name(month, "en")
    return render_template('not_logged_in.html', month=month_name, year=year,
                           days_list=days_list, curr_year=year)


if __name__ == "__main__":
    app.run(debug=True)
