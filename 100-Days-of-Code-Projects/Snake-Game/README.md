# Snake Game 🐍

Classic Snake Game implemented in Python using the `turtle` graphics module and Object-Oriented Programming (OOP).

## 🎮 Description
The snake moves continuously on the screen, eating randomly placed food.  
Each time the snake eats food:
- It grows longer
- The score increases
- The **highest score** is tracked and saved in `data.txt`

The game ends when the snake collides with the wall or with itself. The highest score is persistent across runs.

## ✨ Features
- **Object-Oriented Design** (`Snake`, `Food`, `ScoreBoard` classes)
- **Collision detection** with walls, food, and self
- **High Score persistence** (saved to `data.txt`)
- **Keyboard controls** for movement
- Modular code (separate files for Snake, Food, ScoreBoard)

## 🛠️ Skills Demonstrated
- Python OOP (classes, methods, modularization)
- Graphics programming with `turtle`
- File handling (reading/writing `data.txt` for high score)
- Game loop and event-driven programming
- Collision detection and movement logic

## 📂 Files
- `main.py` – main game loop (controls flow and event handling)
- `snake.py` – defines the `Snake` class (movement, growth, reset)
- `food.py` – defines the `Food` class (random placement)
- `scoreboard.py` – defines the `ScoreBoard` class (score tracking + persistence)
- `data.txt` – stores the highest score

## ▶️ How to Run
1. Clone this repository or navigate to the `Snake-Game` folder.
2. Run:
   ```bash
   python main.py
