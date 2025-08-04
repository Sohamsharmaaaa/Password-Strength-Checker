from flask import Flask, render_template, request, jsonify
import openai
import re
import math
import os
from flask_cors import CORS

# Load API key from environment variable (set yours before running)
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Allows frontend JS requests if needed

# Load password lists safely
def load_wordlist(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            return set(line.strip().lower() for line in f if line.strip())
    except FileNotFoundError:
        print(f"[WARNING] {file_name} not found.")
        return set()

banned = load_wordlist("banned.txt")
weak = load_wordlist("weak_pass.txt")

# Entropy calculation and strength check
leet_map = {'4': 'a', '@': 'a', '3': 'e', '1': 'l', '!': 'i', '0': 'o', '$': 's', '5': 's', '7': 't', '2': 'z'}
patterns = ['qwerty', 'asdf', '1234', 'password', 'letmein']

def normalize_leet(pw):
    return ''.join(leet_map.get(c.lower(), c.lower()) for c in pw)

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[^\w]', password): charset += 32
    return round(len(password) * math.log2(charset), 2) if charset else 0

def check_strength(password):
    pw_lower = password.lower()
    normalized = normalize_leet(password)
    entropy = calculate_entropy(password)
    issues = []

    if pw_lower in banned:
        issues.append("Banned password.")
    if pw_lower in weak:
        issues.append("Weak password from known list.")
    if any(pat in pw_lower for pat in patterns):
        issues.append("Contains keyboard pattern.")
    if entropy < 50:
        issues.append(f"Low entropy: {entropy} bits.")

    # Strength logic
    if any("Banned" in i or "Weak" in i for i in issues):
        strength = "Weak"
    elif issues:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "entropy": entropy,
        "issues": issues
    }

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    password = data.get("password", "")
    result = check_strength(password)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
