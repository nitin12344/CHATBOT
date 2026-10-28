"""
test_chatbot.py
Unit tests for the rule-based chatbot.
"""

import pytest
from chatbot import get_bot_response, match_rule, handle_math, handle_time, handle_date


# ── match_rule ───────────────────────────────────────────────────────────────

class TestMatchRule:
    def test_greeting(self):
        assert match_rule("hello") == "greeting"
        assert match_rule("Hey there!") == "greeting"
        assert match_rule("good morning") == "greeting"

    def test_farewell(self):
        assert match_rule("bye") == "farewell"
        assert match_rule("goodbye see you") == "farewell"

    def test_how_are_you(self):
        assert match_rule("how are you doing?") == "how_are_you"

    def test_joke(self):
        assert match_rule("tell me a joke") == "joke"

    def test_fun_fact(self):
        assert match_rule("give me a fun fact") == "fun_fact"

    def test_motivation(self):
        assert match_rule("i feel sad") == "motivation"
        assert match_rule("motivate me please") == "motivation"

    def test_math(self):
        assert match_rule("calculate 5 + 3") == "math"
        assert match_rule("what is 10 times 4") == "math"

    def test_time(self):
        assert match_rule("what time is it") == "time"

    def test_date(self):
        assert match_rule("what date is it today") == "date"

    def test_python(self):
        assert match_rule("tell me about python") == "python"

    def test_identity(self):
        assert match_rule("what is your name") == "identity"

    def test_fallback(self):
        assert match_rule("xyzzy plugh nonsense input 1234!@#$") == "fallback"


# ── handle_math ──────────────────────────────────────────────────────────────

class TestHandleMath:
    def test_addition(self):
        result = handle_math("calculate 5 + 3")
        assert "8" in result

    def test_subtraction(self):
        result = handle_math("what is 10 - 4")
        assert "6" in result

    def test_multiplication(self):
        result = handle_math("calculate 6 * 7")
        assert "42" in result

    def test_division(self):
        result = handle_math("calculate 20 / 4")
        assert "5" in result

    def test_division_by_zero(self):
        result = handle_math("calculate 10 / 0")
        assert "zero" in result.lower()

    def test_complex_expression(self):
        result = handle_math("calculate (2 + 3) * 4")
        assert "20" in result

    def test_no_expression(self):
        result = handle_math("math please")
        assert "expression" in result.lower() or "compute" in result.lower()


# ── handle_time / handle_date ────────────────────────────────────────────────

class TestTimeDate:
    def test_time_format(self):
        result = handle_time()
        # Should contain AM or PM
        assert "AM" in result or "PM" in result

    def test_date_format(self):
        result = handle_date()
        # Should contain the year
        import datetime
        assert str(datetime.date.today().year) in result


# ── get_bot_response ─────────────────────────────────────────────────────────

class TestGetBotResponse:
    def test_returns_string(self):
        response, exit_flag = get_bot_response("hello")
        assert isinstance(response, str)
        assert isinstance(exit_flag, bool)

    def test_farewell_triggers_exit(self):
        _, should_exit = get_bot_response("bye")
        assert should_exit is True

    def test_normal_does_not_exit(self):
        _, should_exit = get_bot_response("hello")
        assert should_exit is False

    def test_empty_input(self):
        response, exit_flag = get_bot_response("   ")
        assert "type" in response.lower() or "something" in response.lower()
        assert exit_flag is False

    def test_help_command(self):
        response, exit_flag = get_bot_response("help")
        assert "joke" in response.lower()
        assert exit_flag is False

    def test_time_response(self):
        response, _ = get_bot_response("what time is it")
        assert "AM" in response or "PM" in response

    def test_date_response(self):
        response, _ = get_bot_response("what date is it")
        import datetime
        assert str(datetime.date.today().year) in response

    def test_math_response(self):
        response, _ = get_bot_response("calculate 9 + 1")
        assert "10" in response

    def test_case_insensitive(self):
        r1, _ = get_bot_response("HELLO")
        r2, _ = get_bot_response("hello")
        # Both should produce valid (non-fallback) responses
        assert r1 and r2


# ── ChatSession ───────────────────────────────────────────────────────────────

class TestChatSession:
    def test_session_history(self):
        from chatbot import ChatSession
        session = ChatSession(username="Tester")
        session.chat("hello")
        session.chat("tell me a joke")
        assert len(session.history) == 2
        assert session.turn_count == 2

    def test_session_username(self):
        from chatbot import ChatSession
        session = ChatSession(username="Alice")
        assert session.username == "Alice"

    def test_session_exit_on_bye(self):
        from chatbot import ChatSession
        session = ChatSession()
        _, should_exit = session.chat("goodbye")
        assert should_exit is True
