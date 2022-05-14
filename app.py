from flask import Flask, render_template, request
import logic

app = Flask(__name__)


@app.route('/')
def start_page():
    month = int(request.args["month"])
    year = int(request.args["year"])
    day = int(request.args["day"])
    # month = logic.get_curr_month()
    # year = logic.get_curr_year()
    days_list = logic.get_days_list(year, month)
    month_name = logic.month_num_to_name(month, "en")
    return render_template('not_logged_in.html', day=day, month=month_name, year=year,
                           days_list=days_list, curr_year=year)


@app.route('/select_month', methods=["GET"])
def select_month():
    month = int(request.form['months'])
    year = 2022
    month_name = logic.month_num_to_name(month, "en")
    days_list = logic.get_days_list(year, month)
    return render_template('not_logged_in.html', day=10, month=month_name, year=year,
                           days_list=days_list, curr_year=year)


if __name__ == "__main__":
    app.run(debug=True)
