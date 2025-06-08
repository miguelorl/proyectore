from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM datos")
    items = cur.fetchall()
    conn.close()
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
