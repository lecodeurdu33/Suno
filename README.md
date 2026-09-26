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
│   ├── discord.py              # ✅ Publication Discord (webhook)
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
- ✅ **Discord opérationnel** (webhook + embed violet)
- ✅ Modules X et Telegram prêts (stubs)
- ✅ Design sombre violet futuriste

## 🔧 Configuration Discord

1. Sur Discord → Paramètres du serveur → Intégrations → **Webhooks** → Nouveau webhook
2. Copie l’URL du webhook
3. Colle-la dans `config/settings.json` :

```json
{
  "discord": {
    "webhook_url": "https://discord.com/api/webhooks/TON_ID/TON_TOKEN"
  }
}
```

4. Relance le scheduler → les prochaines publications arriveront automatiquement sur Discord avec un bel embed violet Shadow IA.

## 🔮 Roadmap Shadow IA

- [x] Interface web moderne
- [x] Scheduler de base
- [x] Modules multi-plateformes
- [x] Implémentation réelle Discord
- [ ] Implémentation réelle X / Telegram
- [ ] Génération automatique de posts promo avec IA
- [ ] Vue calendrier + drag & drop
- [ ] Statistiques d’écoute Suno
- [ ] Gestion multi-artistes / albums

---
Fait avec ❤️ pour **Shadow IA**
