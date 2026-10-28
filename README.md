# 🤖 Rule-Based Chatbot

A simple yet feature-rich chatbot built in Python using **if-else logic** and **pattern matching** — no machine learning required. Great for understanding the fundamentals of NLP and conversation flow.

---

## 📁 Project Structure

```
CHATBOT/
├── main.py          ← Entry point (run this)
├── chatbot.py       ← Core engine: pattern matching, special handlers, session
├── responses.py     ← All rules, patterns, and responses
├── test_chatbot.py  ← Unit tests (pytest)
└── README.md
```

---

## ⚙️ Requirements

- Python 3.10 or higher
- No external libraries — uses only the Python standard library

Check your Python version:
```bash
python --version
```

---

## 🚀 How to Run

**Step 1 — Clone or download the project**
```bash
git clone <your-repo-url>
cd CHATBOT
```

**Step 2 — Run the chatbot**
```bash
python main.py
```

That's it. No `pip install` needed.

**Step 3 — Enter your name when prompted**
```
  Enter your name (or press Enter to skip): Alice
```

The chatbot will greet you and wait for your input.

---

## 💬 How to Use

Once the chatbot is running, simply type a message and press **Enter**.

```
Alice: hello
ChatBot: Hey there! How can I help you today?

Alice: tell me a joke
ChatBot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

Alice: calculate 10 + 5 * 2
ChatBot: 🔢 10 + 5 * 2 = 20

Alice: what time is it
ChatBot: 🕐 The current time is 03:45 PM.

Alice: bye
ChatBot: Goodbye! Have a wonderful day!
```

### Special commands

| Command     | What it does                              |
|-------------|-------------------------------------------|
| `help`      | Lists all topics the chatbot understands  |
| `history`   | Prints the full conversation so far       |
| `bye` / `quit` | Ends the session                       |

### Topics you can ask about

| Topic           | Example inputs                            |
|-----------------|-------------------------------------------|
| Greetings       | `hello`, `hey`, `good morning`            |
| Identity        | `who are you`, `what is your name`        |
| Jokes           | `tell me a joke`, `make me laugh`         |
| Fun Facts       | `tell me a fact`, `did you know`          |
| Motivation      | `motivate me`, `i feel sad`, `cheer me up`|
| Current Time    | `what time is it`                         |
| Current Date    | `what date is it`, `what day is it`       |
| Math            | `calculate 5 + 3 * 2`, `what is 9 / 3`   |
| Weather         | `how's the weather`, `is it raining`      |
| Python / AI     | `tell me about python`, `are you ai`      |
| Farewell        | `bye`, `quit`, `goodbye`                  |

> The chatbot uses **substring matching**, so you don't need to type exact phrases. "hey can you tell me a joke" works just as well as "tell me a joke".

---

## 🧪 Running Tests

```bash
pytest test_chatbot.py -v
```

If pytest is not installed:
```bash
pip install pytest
pytest test_chatbot.py -v
```

Expected output:
```
33 passed in 0.87s
```

Tests cover rule matching, math evaluation, time/date formatting, session history, and exit signals.

---

## 🏗️ How It Works

```
User Input
    │
    ▼
match_rule()  ←── iterates RULES list, checks if any pattern
    │              is a substring of the (lowercased) input
    ▼
tag (e.g. "joke", "math", "time")
    │
    ▼
get_response(tag)  ←── picks a random response from matching rule
    │
    ▼  (special tokens)
__TIME__  →  handle_time()   — datetime.datetime.now()
__DATE__  →  handle_date()   — datetime.date.today()
__MATH__  →  handle_math()   — regex extraction + safe eval()
    │
    ▼
Response printed to terminal
```

### Key concepts demonstrated
- **Pattern matching** via substring search (simple NLP baseline)
- **Rule-based response selection** with randomisation for variety
- **Special token dispatch** for dynamic responses (time, date, math)
- **Conversation session management** with turn history
- **Safe expression evaluation** using a restricted `eval()` environment

---

## 🔧 Extending the Bot

To add a new topic, open `responses.py` and add a new rule to `RULES`:

```python
{
    "tag": "sports",
    "patterns": ["football", "cricket", "sport", "game", "match"],
    "responses": [
        "Sports are great! What's your favourite?",
        "I love hearing about sports! Tell me more.",
    ],
},
```

No other files need changing — the engine picks it up automatically.
