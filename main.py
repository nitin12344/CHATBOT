"""
main.py
Entry point — runs the interactive chatbot in the terminal.
"""

from chatbot import ChatSession

# ── Styling helpers ──────────────────────────────────────────────────────────

DIVIDER = "─" * 50

BOT_COLOR   = "\033[96m"   # cyan
USER_COLOR  = "\033[93m"   # yellow
RESET       = "\033[0m"
BOLD        = "\033[1m"


def banner() -> None:
    print(f"\n{BOLD}{'':^10}🤖  RULE-BASED CHATBOT  🤖{RESET}")
    print(DIVIDER)
    print("  Type 'help' to see what I can do.")
    print("  Type 'history' to view conversation log.")
    print("  Type 'quit' or 'bye' to exit.")
    print(DIVIDER + "\n")


def prompt_username() -> str:
    name = input("  Enter your name (or press Enter to skip): ").strip()
    return name if name else "You"


# ── Main loop ────────────────────────────────────────────────────────────────

def main() -> None:
    banner()
    username = prompt_username()
    session = ChatSession(username=username)
    print(f"\n  Hello, {username}! I'm ChatBot. Let's chat!\n")
    print(DIVIDER)

    while True:
        try:
            user_input = input(f"{USER_COLOR}{username}: {RESET}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{BOT_COLOR}ChatBot: {RESET}Goodbye! 👋")
            break

        # Special command: print history
        if user_input.lower() == "history":
            session.print_history()
            continue

        # Empty input
        if not user_input:
            print(f"{BOT_COLOR}ChatBot: {RESET}Please type something!\n")
            continue

        # Get response
        response, should_exit = session.chat(user_input)
        print(f"{BOT_COLOR}ChatBot: {RESET}{response}\n")

        if should_exit:
            break

    print(DIVIDER)
    print(f"  Session ended after {session.turn_count} turn(s). See you next time!")
    print(DIVIDER + "\n")


if __name__ == "__main__":
    main()
