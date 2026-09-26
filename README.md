# 🎵 Shadow IA – Suno Scheduler

Interface web + scheduler automatique pour programmer et publier tes chansons Suno sur Discord, X et Telegram.

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

## 📁 Structure du projet

```text
Suno/
├── app.py                      # Interface Flask
├── bots/
│   └── suno_scheduler.py       # Scheduler automatique
├── modules/
│   ├── discord.py              # Publication Discord
│   ├── telegram.py             # Publication Telegram
│   └── twitter.py              # Publication X
├── config/
│   └── settings.json           # Configuration (tokens, webhooks…)
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── songs.db                    # Créé automatiquement
```

## ✨ Fonctionnalités actuelles

- ✅ Ajout de chansons (titre + lien Suno + date/heure)
- ✅ Liste des publications programmées
- ✅ Statut (En attente / Publié)
- ✅ Suppression
- ✅ Scheduler qui vérifie toutes les 30 secondes
- ✅ Modules prêts pour Discord / X / Telegram (stubs)
- ✅ Design sombre violet futuriste

## 🔧 Configuration des publications

1. Ouvre `config/settings.json`
2. Remplis tes tokens / webhooks
3. Complète le code dans `modules/discord.py`, `modules/telegram.py` et `modules/twitter.py`

## 🔮 Roadmap Shadow IA

- [x] Interface web moderne
- [x] Scheduler de base
- [x] Modules multi-plateformes (stubs)
- [ ] Implémentation réelle Discord / X / Telegram
- [ ] Génération automatique de posts promo avec IA
- [ ] Vue calendrier + drag & drop
- [ ] Statistiques d’écoute Suno
- [ ] Gestion multi-artistes / albums

---
Fait avec ❤️ pour **Shadow IA**
