from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS songs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        url TEXT,
        publish_date TEXT,
        published INTEGER DEFAULT 0
    )
    """)

    cur.execute("SELECT * FROM songs ORDER BY publish_date")
    songs = cur.fetchall()

    conn.close()

    return render_template("index.html", songs=songs)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    url = request.form["url"]
    date = request.form["date"]

    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO songs(title,url,publish_date) VALUES(?,?,?)",
        (title, url, date)
    )

    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
