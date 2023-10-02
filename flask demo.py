from flask import Flask, render_template, request
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

app = Flask(__name__, template_folder='.')


@app.route('/', methods=['GET', 'POST'])
def calculate_age_difference():
    if request.method == 'POST':
        user_birthdate = parse(request.form['user_birthdate']).date()
        son_birthdate = parse(request.form['son_birthdate']).date()

        # Calculate the difference in years, months, weeks, and days
        today = datetime.now().date()
        age_difference = relativedelta(today, user_birthdate) - relativedelta(today, son_birthdate)

        return render_template('result.html', age_difference=age_difference)

    return render_template('index.html')


@app.route('/log-click', methods=['POST'])
def log_click():
    x = request.form.get('x')
    y = request.form.get('y')
    log_message = f"[Click Event] Coordinates: ({x}, {y})"
    app.logger.info(log_message)
    return 'OK'


if __name__ == '__main__':
    app.run()