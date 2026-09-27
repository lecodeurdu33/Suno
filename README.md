# 🎵 Shadow IA – Rappels Suno + Messages Discord

## Workflow chanson Suno

1. **Tu programmes** la date/heure dans l’interface
2. **À l’heure H**, Shadow IA t’envoie un rappel Discord :
   > 🔔 C’est l’heure de publier **[Titre]**
3. **Tu ouvres Suno** → Library → ⋮ → **Publish** (1 clic)

La chanson passe de *Link Only* → *Public*.

## 🚀 Installation

```bash
git clone https://github.com/lecodeurdu33/Suno.git
cd Suno
pip install -r requirements.txt
```

## ▶️ Lancement

**Terminal 1 – Interface**
```bash
python app.py
```
→ http://localhost:5000

**Terminal 2 – Scheduler**
```bash
python bots/suno_scheduler.py
```

## 🔧 Webhook Discord

Dans `config/settings.json` :

```json
{
  "discord": {
    "webhook_url": "https://discord.com/api/webhooks/TON_ID/TON_TOKEN"
  }
}
```

## Fonctionnalités

| Fonction | Description |
|----------|-------------|
| Rappel publication | Embed ambre avec lien + instructions Publish |
| Messages Discord | Texte libre programmé (markdown OK) |
| Statut | En attente → 🔔 Notifié |

---
Fait avec ❤️ pour **Shadow IA**
