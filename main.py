from flask import Flask, render_template
import sqlite3
import os

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
    if not os.path.exists(app.config ['UPLOAD_FOLDER']):
        os.makedirs(app.config [ 'UPLOAD_FOLDER'])
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))
