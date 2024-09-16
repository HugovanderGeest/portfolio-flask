import csv
from flask import Flask, render_template, url_for, request, redirect
import mysql.connector
from flask import render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(csvfile)
        writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong!'
    
# Database connectie 
conn = mysql.connector.connect(
    user='geesths', 
    password='NxXY6UbR$/D2nC4P', 
    host='oege.ie.hva.nl', 
    database='zgeesths'
)

@app.route('/intressen')
def intressen():
    try:
        connection = mysql.connector.connect(
            host="oege.ie.hva.nl",
            user="geesths",
            password="NxXY6UbR$/D2nC4P",
            database="zgeesths"
        )
        cursor = connection.cursor()

        # Voert de query uit om alle gegevens uit de tabel personal_interests op te halen
        cursor.execute("SELECT * FROM personal_interests;")
        rows = cursor.fetchall()

        connection.close()
        
        return render_template('personal_interests.html', rows=rows)
    
    except mysql.connector.Error as err:
        return f"Database connection failed. Error: {err}"

# if __name__ == '__main__':
#     from waitress import serve
#     serve(app, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(debug=True)  
