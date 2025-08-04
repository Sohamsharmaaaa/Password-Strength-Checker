# 🔐 Advanced Password Strength Checker

A modern **password strength checker** built with **Flask** (Python) and a responsive **Tailwind CSS frontend**.  
The app calculates password entropy, checks against **weak & banned password lists**, detects **keyboard patterns**,  
and provides a **strength score** (Weak, Moderate, Strong).

---

##  Features
- ✅ **Entropy-based strength calculation**
- ✅ Checks against **banned passwords list**
- ✅ Detects **weak patterns** (e.g., "qwerty", "1234")
- ✅ **Leetspeak normalization** (`p@ssw0rd` → `password`)
- ✅ Responsive **black & blue theme**
- ✅ Smooth scrolling & animations
- ✅ **Dark / Light mode toggle**
- ✅ No passwords are stored or logged

---

##  Installation & Setup

### 1️ Clone this repository
```bash
git clone https://github.com/Sohamsharmaaaa/Password-Strength-Checker.git
cd password_checker
```
### 2️ Install dependencies
```bash

pip install flask flask-cors
```

### 3️ Add password lists
Make sure you have:

banned.txt → list of completely banned passwords
weak_pass.txt → list of weak/common passwords

### 4 Run the Flask server
```bash
python app.py
```
### 5️ Open in browser
Visit:
```bash
http://127.0.0.1:5000/
```

📖 How It Works
User enters a password.

Frontend sends the password to /check route (POST request).

Backend:

Normalizes leetspeak (e.g., @ → a).
Calculates entropy based on character set size.
Checks if it’s in weak or banned list.
Detects common keyboard patterns.
Returns:

Strength (Weak, Moderate, Strong)

Entropy in bits
List of issues found

🎨 Dark & Light Mode
Click the mode toggle button in the navbar to switch between dark and light themes instantly.

⚠️ Security Note
Passwords are never stored or sent to any third-party service.
All checks happen locally on your server.

📜 License
This project is open-source under the MIT License.

✨ Screenshots
(Add screenshots here once the UI is finalized)

🛠 Tech Stack
Backend: Flask (Python)
Frontend: Tailwind CSS
Extra: Smooth scroll, animations, dark mode

---
