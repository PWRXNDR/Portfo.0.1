from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/index.html')
def my_home():
    return render_template('index.html')


# $env:FLASK_APP = "web_server"
# > flask run
#  * Running on http://127.0.0.1:5000/

@app.route('/about.html')
def about_me():
    return render_template('about.html')


@app.route('/components.html')
def components():
    return render_template('components.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/contact.html/thankyou.html')
def thankyou():
    return render_template('thankyou.html')


@app.route('/work.html')
def work():
    return render_template('work.html')


@app.route('/works.html')
def works():
    return render_template('works.html')


@app.route(f'/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'response wasn\'t saved to the database'
    else:
        return 'something went wrong, try again!'
