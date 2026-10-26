<div align="center">

# 🐍 PyTraining

**My daily Python gym — practicing, breaking things, and building real projects along the way.**

![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

</div>

---

## 📖 About

This is where I train — a little Python every day. Some days it's a small script,
other days it's a full mini-project. Nothing here is meant to be "perfect production code":
it's a training log, a sandbox, and a portfolio-in-progress all at once.

---

## 🗂️ What's inside

| Folder | What it is |
|---|---|
| 🧮 [`Lvl-1/Calculator`](./Lvl-1/Calculator) | Desktop calculator built with **Tkinter** — dark theme, keyboard support, error handling |
| 🤖 [`RoutinBot`](./RoutinBot) | **Telegram bot** that sends a daily auto-generated date sticker — `python-telegram-bot`, `APScheduler`, `Pillow` |
| 🛠️ [`BotCraetor`](./BotCraetor) | One idea, two interfaces: a **Desktop** app and a **Telegram bot** (`Telbot`) with an HTML UI |
| 📊 [`Machine-learning`](./Machine-learning) | My full ML learning path — see below |

### 📊 Machine Learning track

Follows the roadmap in [`Machine-learning/Road-Map.MD`](./Machine-learning/Road-Map.MD):

| Stage | Folders |
|---|---|
| Foundations | `OOP`, `numpy`, `Pandas`, `Matplotlib-Seaborn`, `Jupyter-notebook` |
| Preprocessing | `Preprocessing/` — Cleaning, Missing Data, Feature Engineering, Scaling, Encoding, Partitioning |
| Supervised Learning | `Sueprvised-Learning/` — Linear & Logistic Regression, KNN, Decision Tree, Random Forest, SVM, Naive Bayes, Hyperparameter Tuning |
| Libraries | `XGBoost`, `scikit-learn` |

**Up next:** Unsupervised learning (K-Means, DBSCAN, PCA), model evaluation, and deep learning.

---

## 🧠 Skills I'm practicing here

- Core Python — OOP, functions, exception handling
- GUI development with **Tkinter**
- Telegram bot development (async handlers, schedulers)
- Image generation with **Pillow**
- Data analysis with **NumPy**, **Pandas**, **Matplotlib/Seaborn**
- Machine learning with **scikit-learn** and **XGBoost**
- Keeping secrets out of code with `.env` files

---

## 🎯 Current focus (see [`Todo.txt`](./Todo.txt))

A personal exchange-rate app, built step by step: core logic → fast APIs → Figma GUI design → PyQt6 interface → debugging → ship 🚀

---

## 🚀 Running a project

```bash
git clone https://github.com/DashPgi/PyTraining.git
cd PyTraining/<project-folder>
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install <the packages the project imports>
python app.py
```

> Bots (RoutinBot, BotCraetor) need a `.env` file with your own token, e.g. `BOT_TOKEN=...`. Never commit it — it's already in `.gitignore`.

---

## 📜 License

Released under the [MIT License](./LICENSE).