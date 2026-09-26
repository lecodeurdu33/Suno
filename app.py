from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("songs.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            publish_date TEXT NOT NULL,
            published INTEGER DEFAULT 0
        )
    """)

    cur.execute("SELECT * FROM songs ORDER BY publish_date ASC")
    songs = cur.fetchall()
    conn.close()

    return render_template("index.html", songs=songs)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    url = request.form.get("url", "").strip()
    date = request.form.get("date", "").strip()

    if not title or not url or not date:
        return redirect("/")

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO songs (title, url, publish_date) VALUES (?, ?, ?)",
        (title, url, date)
    )
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/delete/<int:song_id>")
def delete(song_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM songs WHERE id = ?", (song_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
