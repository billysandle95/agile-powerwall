"""Unit tests for manual Powerwall push helpers."""

import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src" / "modules"))

import manual_push


class ManualPushTests(unittest.TestCase):
    """Validate behaviour of ``manual_push`` helper utilities."""

    # /**
    #  * Ensure changed tariffs trigger an upload even without forcing.
    #  * Example:
    #  * manual_push.should_push_tariff_data(False, {"import": {"rate": 0.12}})
    #  */
    def test_should_push_when_change_detected(self) -> None:
        """Ensure changed tariffs trigger an upload even without forcing."""

        should_push, reason = manual_push.should_push_tariff_data(
            False, {"import": {"rate": 0.12}}
        )
        self.assertTrue(should_push)
        self.assertEqual(reason, "changed")

    # /**
    #  * Confirm forcing the push succeeds even when no diff exists.
    #  * Example:
    #  * manual_push.should_push_tariff_data(True, {})
    #  */
    def test_should_push_when_forced_without_changes(self) -> None:
        """Confirm forcing the push succeeds even when no diff exists."""

        should_push, reason = manual_push.should_push_tariff_data(True, {})
        self.assertTrue(should_push)
        self.assertEqual(reason, "forced")

    # /**
    #  * Ensure unchanged tariffs without a force flag skip uploads.
    #  * Example:
    #  * manual_push.should_push_tariff_data(False, [])
    #  */
    def test_should_not_push_when_no_change_and_not_forced(self) -> None:
        """Ensure unchanged tariffs without a force flag skip uploads."""

        should_push, reason = manual_push.should_push_tariff_data(False, [])
        self.assertFalse(should_push)
        self.assertEqual(reason, "unchanged")

    # /**
    #  * Validate ``None`` diffs act like unchanged data when not forced.
    #  * Example:
    #  * manual_push.should_push_tariff_data(False, None)
    #  */
    def test_should_not_push_when_none_change_and_not_forced(self) -> None:
        """Validate ``None`` diffs act like unchanged data when not forced."""

        should_push, reason = manual_push.should_push_tariff_data(False, None)
        self.assertFalse(should_push)
        self.assertEqual(reason, "unchanged")

    # /**
    #  * Reject non-boolean ``force_push`` inputs to maintain validation.
    #  * Example:
    #  * manual_push.should_push_tariff_data("yes", None)
    #  */
    def test_invalid_force_flag_raises_value_error(self) -> None:
        """Reject non-boolean ``force_push`` inputs to maintain validation."""

        with self.assertRaises(ValueError):
            manual_push.should_push_tariff_data("yes", None)

    # /**
    #  * Reject unexpected diff types so callers surface useful errors.
    #  * Example:
    #  * manual_push.should_push_tariff_data(False, 42)
    #  */
    def test_invalid_change_type_raises_type_error(self) -> None:
        """Reject unexpected diff types so callers surface useful errors."""

        with self.assertRaises(TypeError):
            manual_push.should_push_tariff_data(False, 42)


if __name__ == "__main__":  # pragma: no cover - manual invocation convenience.
    unittest.main()
