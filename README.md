# 🎮 Tic Tac Toe — Command-Line Game

A simple yet fun **Tic Tac Toe (X-O)** game built using **Python**.
You can play **solo** (against the computer) or **with a friend** — directly in your terminal.

This project demonstrates:
- Clean modular Python code 🧩
- Meaningful docstrings and comments 📘
- Easy replay functionality 🔁
- Minimal dependencies ⚙️
- Persistent score tracking between rounds 🧮

---

## 🕹️ Demo

![Tic Tac Toe Demo](assets/demo.gif)

---

## 📂 Project Structure

```bash
Tic-Tac-Toe-Project/
│
├── assets/
│   └── demo.gif # Animated demo of the game
│
├── src/
│   ├── main.py # Game logic (class-based implementation)
│   └── run.py # Entry point and game loop controller
│
├── requirements.txt # Project dependencies
├── README.md # You're reading it 🙂
└── .gitignore # File to ignore pycache and other unwanted files
```

---

## ⚙️ Installation & Setup

Make sure you have **Python 3.8+** installed on your system.

1. **Clone this repository:**
   ```bash
   git clone https://github.com/maryamtaherifar/Tic-Tac-Toe-Game.git
    ```
2. **Navigate into the project directory:**
    ```bash
    cd Tic-Tac-Toe-Project/src
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Run
You can start the game directly from the terminal using the `run.py` file:


Then simply:

- Choose Solo or With a friend
- Follow the prompts to play!
- You can replay as many times as you like 😄
- After each round, your total scores are automatically updated and displayed.

---

## 🧠 Game Features

- 🎯 Two modes: Solo (vs Computer) or With a Friend
- 🧠 Smart computer moves (blocks and wins strategically)
- 🎨 Colorful terminal UI (powered by termcolor)
- 🎲 Randomized first player (keeps things fair)
- 🔁 Replay option (play again without restarting)
- 🧮 Score tracking: keeps total scores across rounds

---

## 🧩 Dependencies

This project only requires:
- `termcolor` for colorful terminal output

---

## 💡 Future Improvements

- Add difficulty levels (Easy / Hard)
- Implement a graphical UI using tkinter or pygame
- Enable online multiplayer mode (future idea 💭)
