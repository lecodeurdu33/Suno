# 🎵 Shadow IA – Suno + Discord Scheduler

Programme tes chansons Suno **et** des messages Discord libres.

## 🚀 Installation

```bash
git clone https://github.com/lecodeurdu33/Suno.git
cd Suno
pip install -r requirements.txt
```

## ▶️ Lancement

**Terminal 1 – Interface web**
```bash
python app.py
```
→ http://localhost:5000

**Terminal 2 – Scheduler**
```bash
python bots/suno_scheduler.py
```

## ✨ Fonctionnalités

### Chansons Suno
- Ajoute titre + lien + date/heure
- À l’heure prévue → annonce Discord (embed violet) + stubs X/Telegram

### Messages Discord
- Écris un message libre (markdown supporté)
- Programme la date/heure d’envoi
- Le scheduler l’envoie automatiquement via webhook

## 🔧 Configuration Discord

1. Discord → Paramètres serveur → Intégrations → Webhooks → Nouveau webhook
2. Copie l’URL
3. Colle-la dans `config/settings.json` :

```json
{
  "discord": {
    "webhook_url": "https://discord.com/api/webhooks/TON_ID/TON_TOKEN"
  }
}
```

## 📁 Structure

```text
Suno/
├── app.py
├── bots/suno_scheduler.py
├── modules/
│   ├── discord.py          ← chansons + messages libres
│   ├── telegram.py
│   └── twitter.py
├── config/settings.json
├── templates/index.html
└── static/style.css
```

---
Fait avec ❤️ pour **Shadow IA**
