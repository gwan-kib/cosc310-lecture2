"""Exercise 5: Your first tests.

Run them with:      pytest -v

These fail until Cart is implemented. Failing tests can also provide some important information.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercise3 import Cart, OutOfStockError

GYOZA = {"id": 2, "name": "Gyoza (6 pc)", "price": 8.00, "available": True}
RAMEN = {"id": 1, "name": "Tonkotsu Ramen", "price": 16.50, "available": True}
MISO = {"id": 4, "name": "Spicy Miso Ramen", "price": 17.25, "available": False}


def test_empty_cart_total_is_zero() -> None:
    assert Cart().total() == 0


def test_total_across_multiple_items() -> None:
    cart = Cart()
    cart.add_item(GYOZA, 2)      # 16.00
    cart.add_item(RAMEN, 1)      # 16.50
    assert cart.total() == 32.50


def test_adding_same_item_twice_increases_quantity() -> None:
    cart = Cart()
    cart.add_item(GYOZA, 2)
    cart.add_item(GYOZA, 1)
    assert len(cart.lines) == 1
    assert cart.lines[0]["qty"] == 3


def test_zero_quantity_is_rejected() -> None:
    cart = Cart()
    with pytest.raises(ValueError):
        cart.add_item(GYOZA, 0)


def test_unavailable_item_is_rejected() -> None:
    cart = Cart()
    with pytest.raises(OutOfStockError):
        cart.add_item(MISO, 1)


def test_removing_an_absent_item_raises() -> None:
    cart = Cart()
    with pytest.raises(KeyError):
        cart.remove_item(999)


def test_remove_deletes_entire_line_and_preserves_other_items() -> None:
    cart = Cart()
    cart.add_item(GYOZA, 3)
    cart.add_item(RAMEN)
    cart.remove_item(GYOZA["id"])
    assert cart.lines == [{"item_id": 1, "name": RAMEN["name"], "price": 16.50, "qty": 1}]
    assert cart.total() == 16.50


def test_clear_empties_cart() -> None:
    cart = Cart()
    cart.add_item(GYOZA)
    cart.add_item(RAMEN)
    cart.clear()
    assert cart.lines == []
    assert cart.total() == 0.0


def test_rejected_additions_preserve_existing_line() -> None:
    cart = Cart()
    cart.add_item(GYOZA, 2)
    before = [line.copy() for line in cart.lines]
    with pytest.raises(ValueError):
        cart.add_item(GYOZA, -1)
    assert cart.lines == before
    with pytest.raises(OutOfStockError):
        cart.add_item({**GYOZA, "available": False})
    assert cart.lines == before


def test_failed_removal_preserves_existing_items() -> None:
    cart = Cart()
    cart.add_item(GYOZA, 2)
    before = [line.copy() for line in cart.lines]
    with pytest.raises(KeyError):
        cart.remove_item(999)
    assert cart.lines == before


def test_total_rounds_once_after_summing() -> None:
    cart = Cart()
    cart.add_item({**GYOZA, "price": 0.334})
    cart.add_item({**RAMEN, "price": 0.334})
    assert cart.total() == 0.67
