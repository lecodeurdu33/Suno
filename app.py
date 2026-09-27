from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("songs.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
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

    cur.execute("""
        CREATE TABLE IF NOT EXISTS discord_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            publish_date TEXT NOT NULL,
            published INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

@app.route("/")
def index():
    init_db()
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM songs ORDER BY publish_date ASC")
    songs = cur.fetchall()

    cur.execute("SELECT * FROM discord_messages ORDER BY publish_date ASC")
    messages = cur.fetchall()

    conn.close()
    return render_template("index.html", songs=songs, messages=messages)

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

@app.route("/add_message", methods=["POST"])
def add_message():
    content = request.form.get("content", "").strip()
    date = request.form.get("date", "").strip()

    if not content or not date:
        return redirect("/")

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO discord_messages (content, publish_date) VALUES (?, ?)",
        (content, date)
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

@app.route("/delete_message/<int:msg_id>")
def delete_message(msg_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM discord_messages WHERE id = ?", (msg_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)
