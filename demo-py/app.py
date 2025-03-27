from flask import Flask, render_template
import mysql.connector
import time
import os

app = Flask(__name__)

# MySQL Connection Configuration
DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST', 'mysql'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', 'tcomp#mysql'),
    'database': os.getenv('MYSQL_DATABASE', 'school'),
    'port': int(os.getenv('MYSQL_PORT', 3306))
}

# Function to fetch student data
def get_students():
    max_retries = 5
    for i in range(max_retries):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute("SELECT name, roll_number FROM students")
            students = cursor.fetchall()
            cursor.close()
            conn.close()
            return students
        except mysql.connector.Error as e:
            print(f"Database connection failed. Retrying {i+1}/{max_retries}...")
            time.sleep(5)  # Wait 5 seconds before retrying
    return []

# Flask Route
@app.route('/')
def index():
    students = get_students()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)