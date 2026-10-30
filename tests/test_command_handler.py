import unittest
from unittest.mock import patch

from core.command_handler import process_command


class CommandHandlerTests(unittest.TestCase):
    def test_known_utility_returns_structured_response_without_printing(self):
        with patch.dict("core.command_handler.COMMANDS", {"hello": lambda: "Hello there"}):
            result = process_command(" HELLO ")

        self.assertEqual(result["text"], "Hello there")
        self.assertEqual(result["source"], "command")
        self.assertTrue(result["speak"])
        self.assertFalse(result["should_exit"])

    def test_exit_returns_exit_flag(self):
        result = process_command("exit")

        self.assertTrue(result["should_exit"])
        self.assertEqual(result["source"], "command")

    def test_application_command_uses_app_module(self):
        with patch("core.command_handler.open_app", return_value="Opening Chrome.") as opener:
            result = process_command("open chrome")

        opener.assert_called_once_with("chrome")
        self.assertEqual(result["text"], "Opening Chrome.")
        self.assertFalse(result["speak"])

    def test_unknown_command_uses_ai_response(self):
        with patch("core.command_handler.get_ai_response", return_value="AI answer") as ai:
            result = process_command("Explain Python")

        ai.assert_called_once_with("Explain Python")
        self.assertEqual(result["text"], "AI answer")
        self.assertEqual(result["source"], "ai")

    def test_empty_command_does_not_call_ai(self):
        with patch("core.command_handler.get_ai_response") as ai:
            result = process_command("   ")

        ai.assert_not_called()
        self.assertEqual(result["source"], "system")


if __name__ == "__main__":
    unittest.main()
