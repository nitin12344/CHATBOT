"""
responses.py
Predefined rules and responses for the chatbot.
Each rule contains patterns (keywords/phrases) and possible responses.
"""

import random

# ---------------------------------------------------------------------------
# Response rules: list of dicts with "patterns" and "responses"
# Patterns are checked (case-insensitive) against user input.
# ---------------------------------------------------------------------------

RULES = [
    # ── Greetings ──────────────────────────────────────────────────────────
    {
        "tag": "greeting",
        "patterns": ["hello", "hi", "hey", "howdy", "good morning", "good afternoon",
                     "good evening", "sup", "what's up", "greetings"],
        "responses": [
            "Hey there! How can I help you today?",
            "Hello! What's on your mind?",
            "Hi! Great to see you. What can I do for you?",
            "Hey! I'm here and ready to chat.",
        ],
    },

    # ── Farewell ───────────────────────────────────────────────────────────
    {
        "tag": "farewell",
        "patterns": ["bye", "goodbye", "see you", "see ya", "later", "take care",
                     "quit", "exit", "farewell", "cya"],
        "responses": [
            "Goodbye! Have a wonderful day!",
            "See you later! Take care.",
            "Bye! Feel free to chat anytime.",
            "Farewell! It was nice talking to you.",
        ],
    },

    # ── How are you ────────────────────────────────────────────────────────
    {
        "tag": "how_are_you",
        "patterns": ["how are you", "how are you doing", "how do you do",
                     "how's it going", "are you okay", "you okay"],
        "responses": [
            "I'm just a bot, but I'm doing great! Thanks for asking. How about you?",
            "Doing perfectly fine! Ready to help. How are you?",
            "All good on my end! What about you?",
        ],
    },

    # ── User is fine ───────────────────────────────────────────────────────
    {
        "tag": "user_fine",
        "patterns": ["i'm fine", "i am fine", "i'm good", "i am good",
                     "doing well", "i'm great", "pretty good", "not bad"],
        "responses": [
            "That's great to hear!",
            "Glad to know you're doing well!",
            "Awesome! Let me know if there's anything I can help with.",
        ],
    },

    # ── Bot identity ───────────────────────────────────────────────────────
    {
        "tag": "identity",
        "patterns": ["what is your name", "who are you", "what are you",
                     "tell me about yourself", "introduce yourself", "your name"],
        "responses": [
            "I'm ChatBot, a simple rule-based conversational assistant built in Python!",
            "My name is ChatBot. I'm here to answer your questions and keep you company.",
            "I'm ChatBot — your friendly Python-powered assistant!",
        ],
    },

    # ── Creator ────────────────────────────────────────────────────────────
    {
        "tag": "creator",
        "patterns": ["who made you", "who created you", "who built you",
                     "who is your creator", "who developed you"],
        "responses": [
            "I was built by a developer learning Python. Pretty cool, right?",
            "A Python enthusiast created me as a rule-based chatbot project.",
        ],
    },

    # ── Age ────────────────────────────────────────────────────────────────
    {
        "tag": "age",
        "patterns": ["how old are you", "what is your age", "your age"],
        "responses": [
            "I don't have an age — I'm a bot! But I was born the day I was coded.",
            "Age is just a number, and I don't have one. I'm timeless!",
        ],
    },

    # ── Capabilities ───────────────────────────────────────────────────────
    {
        "tag": "capabilities",
        "patterns": ["what can you do", "help me", "what do you know",
                     "your capabilities", "how can you help", "features"],
        "responses": [
            (
                "I can:\n"
                "  • Answer general questions\n"
                "  • Tell jokes\n"
                "  • Share fun facts\n"
                "  • Give motivational quotes\n"
                "  • Chat about the weather (simulated)\n"
                "  • Do basic math\n"
                "  • And much more! Just ask."
            ),
            "I'm a rule-based chatbot. Try asking me for a joke, a fun fact, math, or just say hello!",
        ],
    },

    # ── Jokes ──────────────────────────────────────────────────────────────
    {
        "tag": "joke",
        "patterns": ["tell me a joke", "joke", "make me laugh", "say something funny",
                     "funny", "humor me"],
        "responses": [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "What do you call a fake noodle? An impasta! 🍝",
            "Why can't you give Elsa a balloon? Because she'll let it go! ❄️",
            "I'm reading a book about anti-gravity. It's impossible to put down!",
        ],
    },

    # ── Fun facts ──────────────────────────────────────────────────────────
    {
        "tag": "fun_fact",
        "patterns": ["fun fact", "tell me a fact", "interesting fact",
                     "did you know", "something interesting", "fact"],
        "responses": [
            "🐙 Octopuses have three hearts, and two of them stop beating when they swim!",
            "🍯 Honey never spoils — archaeologists have found 3000-year-old honey in Egyptian tombs!",
            "🌙 A day on Venus is longer than a year on Venus!",
            "🐘 Elephants are the only animals that can't jump.",
            "🎵 Music can help plants grow faster!",
            "🧠 The human brain generates about 20 watts of electricity — enough to power a dim lightbulb.",
        ],
    },

    # ── Motivational quotes ────────────────────────────────────────────────
    {
        "tag": "motivation",
        "patterns": ["motivate me", "inspire me", "quote", "motivation",
                     "i feel sad", "i am sad", "feeling down", "cheer me up",
                     "i need motivation", "feeling low"],
        "responses": [
            "💪 'The only way to do great work is to love what you do.' — Steve Jobs",
            "🌟 'Believe you can and you're halfway there.' — Theodore Roosevelt",
            "🚀 'It does not matter how slowly you go as long as you do not stop.' — Confucius",
            "✨ 'You are never too old to set another goal or dream a new dream.' — C.S. Lewis",
            "🔥 'Push yourself, because no one else is going to do it for you.'",
            "🌈 Every day is a new beginning. Take a deep breath and start again.",
        ],
    },

    # ── Weather (simulated) ────────────────────────────────────────────────
    {
        "tag": "weather",
        "patterns": ["weather", "temperature", "is it raining", "forecast",
                     "how's the weather", "what's the weather"],
        "responses": [
            "I don't have live weather data, but I hope it's sunny where you are! ☀️",
            "I can't check real-time weather, but statistically, every day is a good day to code! 💻",
            "Weather? I wish I could check! Try a weather app for accurate info. 🌤️",
        ],
    },

    # ── Time ───────────────────────────────────────────────────────────────
    {
        "tag": "time",
        "patterns": ["what time is it", "current time", "what's the time", "tell me the time"],
        "responses": ["__TIME__"],  # special token — handled in chatbot.py
    },

    # ── Date ───────────────────────────────────────────────────────────────
    {
        "tag": "date",
        "patterns": ["what date is it", "today's date", "what day is it",
                     "current date", "what is today"],
        "responses": ["__DATE__"],  # special token — handled in chatbot.py
    },

    # ── Math ───────────────────────────────────────────────────────────────
    {
        "tag": "math",
        "patterns": ["calculate", "what is", "math", "solve", "compute",
                     "plus", "minus", "multiply", "divide"],
        "responses": ["__MATH__"],  # special token — handled in chatbot.py
    },

    # ── Python ─────────────────────────────────────────────────────────────
    {
        "tag": "python",
        "patterns": ["python", "programming", "coding", "code", "developer", "software"],
        "responses": [
            "Python is awesome! 🐍 It's one of the most popular languages for data science, AI, and automation.",
            "Love Python! It's readable, powerful, and has a huge community. Great choice!",
            "Coding is a superpower! Keep learning and building amazing things. 🚀",
        ],
    },

    # ── AI / chatbot ───────────────────────────────────────────────────────
    {
        "tag": "ai",
        "patterns": ["artificial intelligence", "machine learning", "deep learning",
                     "neural network", "nlp", "natural language processing",
                     "are you ai", "are you a robot", "are you human"],
        "responses": [
            "I'm not an advanced AI — I use simple rule-based pattern matching. But that's how NLP starts!",
            "Great question! Real AI uses ML models, but I'm powered by if-else logic. Simple but effective!",
            "I'm a rule-based chatbot — no neural networks here, just good old Python conditionals. 😄",
        ],
    },

    # ── Thank you ──────────────────────────────────────────────────────────
    {
        "tag": "thanks",
        "patterns": ["thank you", "thanks", "thank you so much", "many thanks",
                     "thx", "ty", "grateful"],
        "responses": [
            "You're welcome! 😊",
            "Anytime! Happy to help.",
            "No problem at all!",
            "Glad I could help!",
        ],
    },

    # ── Apology ────────────────────────────────────────────────────────────
    {
        "tag": "apology",
        "patterns": ["sorry", "my bad", "i apologize", "pardon", "forgive me"],
        "responses": [
            "No worries at all!",
            "It's completely fine! 😊",
            "No need to apologize — we're good!",
        ],
    },

    # ── Love / like the bot ────────────────────────────────────────────────
    {
        "tag": "love_bot",
        "patterns": ["i love you", "i like you", "you're great", "you are great",
                     "you're awesome", "you are awesome", "you're amazing"],
        "responses": [
            "Aww, that's so sweet! 😊 I like you too!",
            "You're making me blush — if bots could blush! 😄",
            "Thank you! You're pretty awesome yourself!",
        ],
    },

    # ── Default / fallback ─────────────────────────────────────────────────
    {
        "tag": "fallback",
        "patterns": [],  # no patterns — used as last resort
        "responses": [
            "Hmm, I'm not sure I understand. Could you rephrase that?",
            "I didn't quite get that. Try asking me something else!",
            "That's a tricky one! I'm still learning. Try: 'help' to see what I can do.",
            "I'm not sure how to respond to that. Type 'help' for a list of things I can do.",
        ],
    },
]


def get_response(tag: str) -> str:
    """Return a random response for a given tag."""
    for rule in RULES:
        if rule["tag"] == tag:
            return random.choice(rule["responses"])
    return random.choice(RULES[-1]["responses"])  # fallback
