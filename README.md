# 🎵 Shadow IA – Suno Scheduler

Interface web moderne pour programmer et gérer les publications de tes chansons Suno.

## 🚀 Installation

```bash
git clone https://github.com/lecodeurdu33/Suno.git
cd Suno
pip install flask
python app.py
```

Ouvre ensuite : [http://localhost:5000](http://localhost:5000)

## ✨ Fonctionnalités actuelles

- Ajout de chansons avec titre, lien Suno et date/heure de publication
- Liste des publications programmées
- Statut (En attente / Publié)
- Suppression d’une publication
- Design sombre violet futuriste (thème Shadow IA)

## 📁 Structure

```text
Suno/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── songs.db          # créé automatiquement
```

## 🔮 Prochaines étapes (Shadow IA)

- [ ] Scheduler automatique (`bots/suno_scheduler.py`)
- [ ] Publication Discord / X / Telegram
- [ ] Génération de posts promo avec IA
- [ ] Vue calendrier + drag & drop
- [ ] Statistiques d’écoute Suno

---
Fait avec ❤️ pour Shadow IA
