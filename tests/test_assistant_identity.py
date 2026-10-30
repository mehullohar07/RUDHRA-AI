import io
import unittest
from contextlib import redirect_stdout

from core.assistant import ASSISTANT_NAME, VERSION, banner


class AssistantIdentityTests(unittest.TestCase):
    def test_identity_and_version(self):
        self.assertEqual(ASSISTANT_NAME, "RUDHRA AI")
        self.assertEqual(VERSION, "0.6.0")

    def test_banner_uses_current_identity_and_version(self):
        output = io.StringIO()
        with redirect_stdout(output):
            banner()
        self.assertIn(ASSISTANT_NAME, output.getvalue())
        self.assertIn(f"Version {VERSION}", output.getvalue())


if __name__ == "__main__":
    unittest.main()
