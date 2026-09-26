"""
Shadow IA - Suno Scheduler
Vérifie les publications programmées et les envoie sur Discord / X / Telegram.
"""

import sys
import sqlite3
import time
from datetime import datetime
from pathlib import Path

# Ajoute le dossier racine du projet au PYTHONPATH
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

# Modules de publication
from modules.discord import publish_to_discord
from modules.telegram import publish_to_telegram
from modules.twitter import publish_to_x

# Chemin de la base de données (même dossier que app.py)
DB_PATH = ROOT_DIR / "songs.db"

def get_pending_songs():
    """Récupère les chansons dont la date de publication est passée et non encore publiées."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%dT%H:%M")

    cur.execute("""
        SELECT * FROM songs
        WHERE published = 0
          AND publish_date <= ?
        ORDER BY publish_date ASC
    """, (now,))

    songs = cur.fetchall()
    conn.close()
    return songs

def mark_as_published(song_id: int):
    """Marque une chanson comme publiée."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE songs SET published = 1 WHERE id = ?", (song_id,))
    conn.commit()
    conn.close()

def process_song(song):
    """Traite une chanson : publication + marquage."""
    title = song["title"]
    url = song["url"]
    song_id = song["id"]

    print(f"\n🎵 Publication : {title}")
    print(f"   Lien : {url}")

    # --- Publication multi-plateformes ---
    success = False

    try:
        if publish_to_discord(title, url):
            success = True
    except Exception as e:
        print(f"   [Discord] Exception : {e}")

    try:
        if publish_to_x(title, url):
            success = True
    except Exception as e:
        print(f"   [X] Exception : {e}")

    try:
        if publish_to_telegram(title, url):
            success = True
    except Exception as e:
        print(f"   [Telegram] Exception : {e}")

    if success:
        mark_as_published(song_id)
        print(f"   📌 Marqué comme publié (id={song_id})")
    else:
        print("   ⚠️ Aucune plateforme n'a réussi → non marqué comme publié")

def run_scheduler(interval_seconds: int = 30):
    """Boucle principale du scheduler."""
    print("=" * 50)
    print("🚀 Shadow IA – Suno Scheduler démarré")
    print(f"   Vérification toutes les {interval_seconds} secondes")
    print("=" * 50)

    while True:
        try:
            pending = get_pending_songs()

            if pending:
                print(f"\n[{datetime.now().strftime('%H:%M:%S')}] {len(pending)} publication(s) à traiter")
                for song in pending:
                    process_song(song)
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Aucune publication en attente", end="\r")

        except Exception as e:
            print(f"\n❌ Erreur scheduler : {e}")

        time.sleep(interval_seconds)

if __name__ == "__main__":
    run_scheduler(interval_seconds=30)
