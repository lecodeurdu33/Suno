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
    """Charge la configuration depuis settings.json."""
    try:
        with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"   [Discord] Erreur lecture config : {e}")
        return {}


def publish_to_discord(title: str, url: str) -> bool:
    """
    Publie une chanson sur Discord via webhook.
    Retourne True si succès, False sinon.
    """
    settings = load_settings()
    webhook_url = settings.get("discord", {}).get("webhook_url", "").strip()

    if not webhook_url:
        print("   [Discord] ⚠️  Webhook non configuré dans config/settings.json")
        return False

    # Message avec embed stylé Shadow IA
    payload = {
        "username": "Shadow IA",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/2995/2995101.png",
        "embeds": [
            {
                "title": f"🎵 {title}",
                "description": f"Nouvelle sortie Suno !\n\n[Écouter sur Suno]({url})",
                "url": url,
                "color": 0x7C3AED,  # Violet Shadow IA
                "footer": {
                    "text": "Shadow IA • Publication automatique"
                }
            }
        ]
    }

    try:
        response = requests.post(webhook_url, json=payload, timeout=10)

        if response.status_code in (200, 204):
            print(f"   [Discord] ✅ Publié : {title}")
            return True
        else:
            print(f"   [Discord] ❌ Erreur {response.status_code} : {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"   [Discord] ❌ Erreur réseau : {e}")
        return False
