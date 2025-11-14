import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src" / "modules"))

import manual_push


def test_should_push_when_change_detected():
    # Example usage ensures change triggers push even without force flag.
    should_push, reason = manual_push.should_push_tariff_data(
        False, {"import": {"rate": 0.12}}
    )
    assert should_push is True
    assert reason == "changed"


def test_should_push_when_forced_without_changes():
    should_push, reason = manual_push.should_push_tariff_data(True, {})
    assert should_push is True
    assert reason == "forced"


def test_should_not_push_when_no_change_and_not_forced():
    should_push, reason = manual_push.should_push_tariff_data(False, [])
    assert should_push is False
    assert reason == "unchanged"


def test_invalid_force_flag_raises_value_error():
    with pytest.raises(ValueError):
        manual_push.should_push_tariff_data("yes", None)


def test_invalid_change_type_raises_type_error():
    with pytest.raises(TypeError):
        manual_push.should_push_tariff_data(False, 42)
