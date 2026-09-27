"""
Module Discord pour Shadow IA.
- Rappel « C'est l'heure de publier »
- Annonce chanson
- Messages libres programmés
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


def _post(payload: dict) -> bool:
    webhook_url = _get_webhook()
    if not webhook_url:
        print("   [Discord] ⚠️  Webhook non configuré dans config/settings.json")
        return False
    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        if response.status_code in (200, 204):
            return True
        print(f"   [Discord] ❌ Erreur {response.status_code} : {response.text[:120]}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"   [Discord] ❌ Réseau : {e}")
        return False


def send_publish_reminder(title: str, url: str) -> bool:
    """
    Envoie le rappel principal :
    « C'est l'heure de publier [Titre] » + instructions Suno.
    """
    payload = {
        "username": "Shadow IA",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/2995/2995101.png",
        "embeds": [{
            "title": f"🔔 C'est l'heure de publier : {title}",
            "description": (
                f"Ta chanson est prête à passer en **Public** sur Suno.\n\n"
                f"**Lien :** [Ouvrir sur Suno]({url})\n\n"
                f"**À faire (1 clic) :**\n"
                f"1. Ouvre Suno → **Library**\n"
                f"2. Clique sur **⋮** à côté de la chanson\n"
                f"3. Appuie sur **Publish**\n\n"
                f"Ensuite elle sera visible sur ton profil et en découverte."
            ),
            "url": url,
            "color": 0xFBBF24,  # Ambre = rappel
            "footer": {"text": "Shadow IA • Rappel de publication"}
        }]
    }

    ok = _post(payload)
    if ok:
        print(f"   [Discord] ✅ Rappel envoyé : {title}")
    return ok


def publish_to_discord(title: str, url: str) -> bool:
    """Annonce post-publication (optionnelle)."""
    payload = {
        "username": "Shadow IA",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/2995/2995101.png",
        "embeds": [{
            "title": f"🎵 {title}",
            "description": f"Nouvelle sortie Suno !\n\n[Écouter sur Suno]({url})",
            "url": url,
            "color": 0x7C3AED,
            "footer": {"text": "Shadow IA • Publication"}
        }]
    }
    ok = _post(payload)
    if ok:
        print(f"   [Discord] ✅ Annonce : {title}")
    return ok


def send_discord_message(content: str) -> bool:
    """Message texte libre programmé."""
    payload = {
        "username": "Shadow IA",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/2995/2995101.png",
        "content": content
    }
    ok = _post(payload)
    if ok:
        print(f"   [Discord] ✅ Message libre envoyé")
    return ok
