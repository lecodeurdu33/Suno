"""
Module de publication Discord pour Shadow IA.
Utilise un webhook Discord (configuré dans config/settings.json).
"""

import json
from pathlib import Path
import requests

ROOT_DIR = Path(__file__).parent.parent
SETTINGS_PATH = ROOT_DIR / "config" / "settings.json"


def load_settings() -> dict:
    try:
        with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"   [Discord] Erreur lecture config : {e}")
        return {}


def _get_webhook() -> str:
    settings = load_settings()
    return settings.get("discord", {}).get("webhook_url", "").strip()


def publish_to_discord(title: str, url: str) -> bool:
    """Publie une chanson Suno (embed stylé)."""
    webhook_url = _get_webhook()
    if not webhook_url:
        print("   [Discord] ⚠️  Webhook non configuré")
        return False

    payload = {
        "username": "Shadow IA",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/2995/2995101.png",
        "embeds": [{
            "title": f"🎵 {title}",
            "description": f"Nouvelle sortie Suno !\n\n[Écouter sur Suno]({url})",
            "url": url,
            "color": 0x7C3AED,
            "footer": {"text": "Shadow IA • Publication automatique"}
        }]
    }

    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        if response.status_code in (200, 204):
            print(f"   [Discord] ✅ Chanson : {title}")
            return True
        print(f"   [Discord] ❌ Erreur {response.status_code}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"   [Discord] ❌ Réseau : {e}")
        return False


def send_discord_message(content: str) -> bool:
    """Envoie un message texte libre (ou avec markdown) sur Discord."""
    webhook_url = _get_webhook()
    if not webhook_url:
        print("   [Discord] ⚠️  Webhook non configuré")
        return False

    payload = {
        "username": "Shadow IA",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/2995/2995101.png",
        "content": content
    }

    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        if response.status_code in (200, 204):
            print(f"   [Discord] ✅ Message envoyé")
            return True
        print(f"   [Discord] ❌ Erreur {response.status_code} : {response.text[:100]}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"   [Discord] ❌ Réseau : {e}")
        return False
