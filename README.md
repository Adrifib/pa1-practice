# Three-in-a-Row Game

## 📚 **Programming and Algorithms 1**
**Bachelor's Degree in Artificial Intelligence**  
*Instructors:* Jordi Delgado & José Luis Balcázar  
*Practice:* Teamwork Project, November 2024

---

## 📝 **Project Overview**
This project focuses on developing an *"abstract board"* that allows players to play the classic **Three-in-a-Row** game ([Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-tac-toe)), along with potential variations.

Initially, the program will support two human players interacting with the board via a functional programming style, using **nonlocal declarations** to achieve closure effects.

---

## 📆 **Submission Deadline**
- **Date:** January 13, 2025
- **Deliverables:**
  - Complete Python code (*abs_board.py* and any other supporting scripts).
  - A report explaining:
    - Why the submitted code is a correct solution.
    - Main challenges faced and how they were addressed.
    - Task distribution among team members.

---

## 🎮 **Game Description**
The game is played in **two phases:**
1. **Placement Phase:** Players place their pieces on the board.
2. **Movement Phase:** Once all pieces are placed, players move their pieces to empty spaces.

### Default Configuration:
- **Board Size:** 3x3
- **Pieces per Player:** 4

The program should be designed to allow easy configuration of board size and piece count.

**General Rule Suggestion:** For an NxN board, each player should have approximately \((N^2 - 1) / 2\) pieces.

---

## 🛠️ **Program Structure**
The project must include:
1. **Abstract Board Implementation:** (*abs_board.py*)
2. **Driver Programs:** Text-based and graphical (using **Pygame**) drivers to allow two human players to interact with the board.

- Initial driver programs will be provided to guide development.
- Teams must implement the abstract board to be compatible with these drivers.
- Additional drivers or functionality can be added if desired.

**Note:** Only an incomplete abstract board file (*abs_board_h.py*) will be provided as a starting point.

---

## 🎲 **Game Variants**
### Suggested Variants:
1. **Standard:** The first player to align three pieces wins.
2. **Misery (Reverse Tic-Tac-Toe):** The first player to align three pieces loses ([Misère Game](https://en.wikipedia.org/wiki/Mis%C3%A8re)).

Additional variants are encouraged but not required. All decisions regarding variants must be documented in the final report.

---

## 🤝 **Team Collaboration**
- Teams must consist of **two members**.
- The final report must outline each member's contributions, detailing tasks and responsibilities.

---

## 📄 **Deliverables Summary**
1. **Code Files:** Complete implementation of the abstract board and functional driver programs.
2. **Report:** Detailing:
   - Code correctness analysis.
   - Challenges and solutions.
   - Task distribution.
   - Additional implemented features (if any).

---

## 🚀 **Getting Started**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/three-in-a-row.git
   ```
2. Run the text-based driver:
   ```bash
   python text_driver.py
   ```
3. Run the graphical driver (if available):
   ```bash
   python pygame_driver.py
   ```

---

## 📚 **Resources**
- [Tic-Tac-Toe Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe)
- [Misère Game Wikipedia](https://en.wikipedia.org/wiki/Mis%C3%A8re)
- Python Documentation: [Python.org](https://www.python.org/)

---

## 🧑‍💻 **Authors**
- **Team Member 1**
- **Team Member 2**

---

*Happy coding and good luck!* 🚀✨


