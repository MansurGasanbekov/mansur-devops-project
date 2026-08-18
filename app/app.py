import os
import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    cur = conn.cursor()
    cur.execute("SELECT name FROM users ORDER BY id")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return "<h1>Mansur DevOps Project</h1><p>Users:</p><ul>" + \
           "".join(f"<li>{user[0]}</li>" for user in users) + \
           "</ul>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
