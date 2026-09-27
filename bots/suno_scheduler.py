"""
Shadow IA - Scheduler

Workflow chanson Suno :
1. Tu programmes date/heure
2. À l'heure H → rappel Discord : « C'est l'heure de publier [Titre] »
3. Tu ouvres Suno → Library → ⋮ → Publish (1 clic)

+ Messages Discord libres programmés
"""

import sys
import sqlite3
import time
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from modules.discord import send_publish_reminder, send_discord_message

DB_PATH = ROOT_DIR / "songs.db"


def get_pending_songs():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%dT%H:%M")
    cur.execute("""
        SELECT * FROM songs
        WHERE published = 0 AND publish_date <= ?
        ORDER BY publish_date ASC
    """, (now,))
    rows = cur.fetchall()
    conn.close()
    return rows


def get_pending_messages():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%dT%H:%M")
    cur.execute("""
        SELECT * FROM discord_messages
        WHERE published = 0 AND publish_date <= ?
        ORDER BY publish_date ASC
    """, (now,))
    rows = cur.fetchall()
    conn.close()
    return rows


def mark_song_notified(song_id: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE songs SET published = 1 WHERE id = ?", (song_id,))
    conn.commit()
    conn.close()


def mark_message_published(msg_id: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE discord_messages SET published = 1 WHERE id = ?", (msg_id,))
    conn.commit()
    conn.close()


def process_song(song):
    """Envoie le rappel « C'est l'heure de publier »."""
    title = song["title"]
    url = song["url"]
    song_id = song["id"]

    print(f"\n🔔 Rappel publication : {title}")
    print(f"   Lien : {url}")

    try:
        if send_publish_reminder(title, url):
            mark_song_notified(song_id)
            print(f"   📌 Rappel envoyé → marqué notifié (id={song_id})")
            print(f"   → À faire : Suno → Library → ⋮ → Publish")
        else:
            print("   ⚠️ Échec envoi rappel → non marqué")
    except Exception as e:
        print(f"   ❌ Exception : {e}")


def process_message(msg):
    content = msg["content"]
    msg_id = msg["id"]

    print(f"\n💬 Message Discord : {content[:60]}{'...' if len(content) > 60 else ''}")

    try:
        if send_discord_message(content):
            mark_message_published(msg_id)
            print(f"   📌 Message envoyé (id={msg_id})")
        else:
            print("   ⚠️ Échec → non marqué")
    except Exception as e:
        print(f"   ❌ Exception : {e}")


def run_scheduler(interval_seconds: int = 30):
    print("=" * 55)
    print("🚀 Shadow IA – Scheduler démarré")
    print(f"   Vérification toutes les {interval_seconds}s")
    print()
    print("   Workflow chanson :")
    print("   1. Tu programmes la date/heure")
    print("   2. À l'heure H → rappel Discord")
    print("      « C'est l'heure de publier [Titre] »")
    print("   3. Tu ouvres Suno → Publish (1 clic)")
    print()
    print("   + Messages Discord libres programmés")
    print("=" * 55)

    while True:
        try:
            songs = get_pending_songs()
            messages = get_pending_messages()

            if songs or messages:
                print(f"\n[{datetime.now().strftime('%H:%M:%S')}] "
                      f"{len(songs)} rappel(s) + {len(messages)} message(s)")

                for song in songs:
                    process_song(song)

                for msg in messages:
                    process_message(msg)
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] En attente...", end="\r")

        except Exception as e:
            print(f"\n❌ Erreur scheduler : {e}")

        time.sleep(interval_seconds)


if __name__ == "__main__":
    run_scheduler(interval_seconds=30)
