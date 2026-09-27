import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")


class PublicStaticBoundaryTests(unittest.TestCase):
    def test_no_client_side_password_gate(self):
        self.assertNotIn('type="password"', INDEX)
        self.assertNotIn("CORRECT_PASS", INDEX)
        self.assertNotIn("Nova2026", INDEX)

    def test_demo_entry_is_explicit(self):
        self.assertIn("enterDemo()", INDEX)
        self.assertIn("Public interactive prototype", INDEX)

    def test_no_local_secret_language(self):
        self.assertNotIn("ACCESS RESTRICTED", INDEX)


if __name__ == "__main__":
    unittest.main()
