# **🪨 Rock, Paper, Scissors Game**
### A simple **Python-based** game where users compete against the computer in the classic **Rock, Paper, Scissors** battle.

## **🚀 Project Overview**
This project implements a **Rock, Paper, Scissors** game using Python. The user selects **rock**, **paper**, or **scissors**, while the computer randomly picks a move. The program then determines the winner based on standard game rules.  

### **🔹 Features**
✅ **User vs. Computer gameplay**  
✅ **Randomized computer moves**  
✅ **Automatic winner detection**  
✅ **Modular code structure for better maintainability**  

## **📁 Folder Structure**
```
rock-paper-scissors/
│── game.py         # Main game loop
│── choices/        # Folder containing choice modules
│   │── __init__.py  # Makes "choices" a package
│   │── rock.py      # Rock logic
│   │── paper.py     # Paper logic
│   │── scissors.py  # Scissors logic
│── utils.py        # Helper functions
│── README.md       # Documentation file
```

## **💻 Installation & Setup**
### **🔹 Prerequisites**
Ensure you have **Python 3.7+** installed.  

### **🔹 Running the Game**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Python-Game.git
   cd Python-Game
   ```
2. **Run the game**:
   ```bash
   python game.py
   ```

## **🎮 Gameplay Rules**
- **Rock beats Scissors**  
- **Scissors beat Paper**  
- **Paper beats Rock**  
- **If both players pick the same choice, it's a tie!**  

## **📜 Code Explanation**
### **1️⃣ `game.py` (Main Game Logic)**
- Handles **user input** and **calls functions from choice files**.
- Displays **results** after determining the winner.

### **2️⃣ `choices/rock.py`, `choices/paper.py`, `choices/scissors.py`**
- Each file contains logic to check whether it **beats the opponent's choice**.

### **3️⃣ `utils.py` (Helper Functions)**
- Includes functions for **computer’s random choice** and **winner determination**.

## **⚠️ Common Errors & Fixes**
### **1️⃣ Invalid User Input**
✅ **Issue:** If a user enters something other than **rock, paper, or scissors**, the program crashes.  
✅ **Fix:** **Validate input** before processing.  

### **2️⃣ Unexpected Behavior in Winner Calculation**
✅ **Issue:** Sometimes the winner isn't correctly determined.  
✅ **Fix:** Ensure **conditions match game rules accurately**.  

## **📜 License**
This project is open-source under the **MIT License**. Feel free to modify and distribute.  
