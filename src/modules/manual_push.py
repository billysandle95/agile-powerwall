"""Utility helpers for manual Powerwall tariff pushes."""

from collections.abc import Mapping, Sequence
from typing import Any, Tuple


# /**
#  * Determine whether a tariff update should be pushed to the Powerwall.
#  * @param {bool} force_push - When True, always allow the push even if there are no changes.
#  * @param {Any} tariff_change - The calculated diff describing tariff changes.
#  * @returns {(bool, str)} A tuple describing if a push is required and the reason.
#  */
def should_push_tariff_data(force_push: bool, tariff_change: Any) -> Tuple[bool, str]:
    """Return whether the tariff should be pushed and the associated reason.

    Example:
        >>> should_push_tariff_data(True, {"import": {"price": 0.12}})
        (True, 'changed')
    """
    if not isinstance(force_push, bool):
        raise ValueError("force_push must be a boolean value")

    if tariff_change is None:
        return force_push, "forced" if force_push else "unchanged"

    if isinstance(tariff_change, Mapping):
        is_empty = len(tariff_change) == 0
    elif isinstance(tariff_change, Sequence) and not isinstance(
        tariff_change, (str, bytes, bytearray)
    ):
        is_empty = len(tariff_change) == 0
    else:
        raise TypeError("tariff_change must be a mapping, sequence, or None")

    if not is_empty:
        return True, "changed"

    if force_push:
        return True, "forced"

    return False, "unchanged"


# Example usage:
# should_push_tariff_data(False, [])
