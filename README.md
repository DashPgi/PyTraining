<div align="center">

# 🐍 PyTraining

**My daily Python gym — practicing, breaking things, and building small projects along the way.**

![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white)
![Status](https://img.shields.io/badge/status-active-brightgreen)

</div>

---

## 📖 About

This is where I train — every day, a little bit of Python. Some days it's a small script,
other days it's a full mini-project. Nothing here is meant to be "perfect production code" —
it's a training log, a sandbox, and a portfolio-in-progress all at once.

---

## 🗂️ What's inside

| Project / Folder | What it is |
|---|---|
| 🧮 [`Lvl-1/Calculator`](./Lvl-1/Calculator) | A desktop calculator built with **Tkinter**, styled with a dark theme, full keyboard support, and error handling (division by zero, invalid expressions, etc.) |
| 🤖 [`RoutinBot`](./RoutinBot) | A **Telegram bot** that sends a daily auto-generated date/reminder sticker on a schedule — built with `python-telegram-bot`, `APScheduler`, and `Pillow` for image generation |
| 🛠️ [`BotCraetor`](./BotCraetor) | An app with **two versions**: a Desktop version and a Telegram bot version of the same idea — exploring how the same logic can power different interfaces |
| 📊 [`Machine-learning`](./Machine-learning) | My personal ML learning space — NumPy, Pandas, Matplotlib/Seaborn, OOP fundamentals, and Jupyter notebooks, following the roadmap in [`Machine-learning/Road-Map.MD`](./Machine-learning/Road-Map.MD) |

---

## 🧠 Skills I'm practicing here

- Core Python (variables, control flow, functions, OOP, exception handling)
- GUI development with **Tkinter**
- Telegram bot development (`python-telegram-bot`, async handlers, schedulers)
- Image generation & manipulation with **Pillow**
- Data analysis foundations: **NumPy**, **Pandas**, **Matplotlib/Seaborn**
- Working with `.env` files and environment variables for secrets

---

## 🎯 Current focus (see [`Todo.txt`](./Todo.txt))

I'm currently working on a personal finance/exchange-rate app, step by step:
1. Build the core computation logic
2. Integrate the fastest & most reliable APIs
3. Design a clean GUI in Figma
4. Rebuild the GUI in **PyQt6**
5. Debug and refine with AI pair-programming
6. Ship a polished, working app 🚀

---

## 🚀 Running a project

Each sub-project is self-contained. General steps:

```bash
git clone https://github.com/DashPgi/PyTraining.git
cd PyTraining/<project-folder>
pip install -r requirements.txt   # if present
python app.py
```

> Some projects (like RoutinBot) require a `.env` file with your own bot token — see the project's code for the expected variable names.

---

## 🤝 Notes

This repo will keep growing as I keep training. If you spot something that could be cleaner or more Pythonic, issues and suggestions are always welcome!
