"""
chatbot.py
Core chatbot engine — handles pattern matching, special tokens,
and conversation flow.
"""

import re
import datetime
from responses import RULES, get_response


# ---------------------------------------------------------------------------
# Pattern matching
# ---------------------------------------------------------------------------

def match_rule(user_input: str) -> str:
    """
    Compare user input against all rules and return the matching tag.
    Uses substring matching (case-insensitive).
    Falls back to 'fallback' tag if nothing matches.
    """
    text = user_input.lower().strip()

    for rule in RULES:
        if not rule["patterns"]:
            continue  # skip fallback during pattern scan
        for pattern in rule["patterns"]:
            if pattern in text:
                return rule["tag"]

    return "fallback"


# ---------------------------------------------------------------------------
# Special token handlers
# ---------------------------------------------------------------------------

def handle_time() -> str:
    now = datetime.datetime.now()
    return f"🕐 The current time is {now.strftime('%I:%M %p')}."


def handle_date() -> str:
    today = datetime.date.today()
    return f"📅 Today is {today.strftime('%A, %B %d, %Y')}."


def handle_math(user_input: str) -> str:
    """
    Extract and safely evaluate a simple arithmetic expression from user input.
    Supports: + - * / ** and parentheses.
    """
    # Extract the expression — look for numbers and operators
    expression = re.sub(r"[^0-9+\-*/().\s]", "", user_input).strip()

    if not expression:
        return "Please give me a math expression like: 'calculate 5 + 3 * 2'"

    try:
        # Restrict eval to safe math only
        allowed = {
            "__builtins__": {},
            "abs": abs,
            "round": round,
            "pow": pow,
        }
        result = eval(expression, allowed)  # noqa: S307
        return f"🔢 {expression} = {result}"
    except ZeroDivisionError:
        return "⚠️ Oops! Division by zero is not allowed."
    except Exception:
        return (
            f"⚠️ I couldn't compute '{expression}'. "
            "Try something like: 'calculate 10 + 5' or 'what is 3 * 7'"
        )


# ---------------------------------------------------------------------------
# Special keyword shortcuts
# ---------------------------------------------------------------------------

SHORTCUTS = {
    "help": (
        "\n📖 Here's what you can ask me:\n"
        "  • Greetings      — hi, hello, hey\n"
        "  • Identity       — who are you, what is your name\n"
        "  • Jokes          — tell me a joke\n"
        "  • Fun facts      — tell me a fact\n"
        "  • Motivation     — motivate me, i feel sad\n"
        "  • Time & Date    — what time is it, what date is it\n"
        "  • Math           — calculate 5 + 3, what is 10 * 7\n"
        "  • Weather        — how's the weather\n"
        "  • Python / AI    — tell me about python\n"
        "  • Farewell       — bye, goodbye, quit\n"
        "\nType 'quit' or 'bye' to exit.\n"
    )
}


# ---------------------------------------------------------------------------
# Main chat function
# ---------------------------------------------------------------------------

def get_bot_response(user_input: str) -> tuple[str, bool]:
    """
    Process user input and return (response_text, should_exit).
    should_exit is True when the user wants to quit.
    """
    text = user_input.strip()

    if not text:
        return "Please type something! I'm listening. 👂", False

    # Shortcut commands (exact match)
    lower = text.lower()
    if lower in SHORTCUTS:
        return SHORTCUTS[lower], False

    # Match against rules
    tag = match_rule(text)

    # Handle farewell (exit signal)
    if tag == "farewell":
        return get_response("farewell"), True

    # Handle special token responses
    response = get_response(tag)

    if response == "__TIME__":
        return handle_time(), False

    if response == "__DATE__":
        return handle_date(), False

    if response == "__MATH__":
        return handle_math(text), False

    return response, False


# ---------------------------------------------------------------------------
# Conversation history
# ---------------------------------------------------------------------------

class ChatSession:
    """Manages a single conversation session with history."""

    def __init__(self, username: str = "You"):
        self.username = username
        self.history: list[dict] = []
        self.turn_count = 0

    def chat(self, user_input: str) -> tuple[str, bool]:
        """Process one turn. Returns (bot_response, should_exit)."""
        self.turn_count += 1
        response, should_exit = get_bot_response(user_input)

        self.history.append({
            "turn": self.turn_count,
            "user": user_input,
            "bot": response,
        })

        return response, should_exit

    def print_history(self) -> None:
        """Print the full conversation history."""
        if not self.history:
            print("No conversation history yet.")
            return
        print("\n── Conversation History ──")
        for entry in self.history:
            print(f"  [{entry['turn']}] {self.username}: {entry['user']}")
            print(f"       Bot: {entry['bot']}")
        print("──────────────────────────\n")
