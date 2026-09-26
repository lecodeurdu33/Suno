"""
Module de publication Discord pour Shadow IA.
À configurer avec un webhook Discord.
"""

def publish_to_discord(title: str, url: str):
    """
    Publie une chanson sur Discord via webhook.
    Remplace WEBHOOK_URL par ton vrai webhook.
    """
    # TODO: Implémenter avec requests + webhook
    # Exemple :
    # import requests
    # webhook_url = "https://discord.com/api/webhooks/..."
    # payload = {
    #     "content": f"🎵 **Nouvelle sortie !**\n**{title}**\n{url}"
    # }
    # requests.post(webhook_url, json=payload)

    print(f"   [Discord] → {title}")
    # Pour l'instant on simule juste le succès
    return True
