import calendar
from flask import Flask, request, render_template
from datetime import datetime
import locale

# Устанавливаем русскую локаль
locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')

app = Flask(__name__)


@app.route('/')
def main_page():
    current_date = datetime.now()
    year = current_date.year
    month_for_calendar = current_date.month
    month = current_date.strftime('%B')
    current_day = current_date.day
    week_number = current_date.isocalendar()[1]
    days_in_month = calendar.monthrange(year, month_for_calendar)[1]

    return render_template('main_page.html', year=year, month=month, current_day=current_day, week_number=week_number,
                           days_in_month=days_in_month)


if __name__ == '__main__':
    app.run(debug=True)
