from exercise1 import available_under, load_menu


def test_filter_excludes_unavailable_and_exact_limit_and_sorts() -> None:
    menu = [
        {"price": 8.0, "available": True},
        {"price": 1.0, "available": False},
        {"price": 10.0, "available": True},
        {"price": 3.25, "available": True},
    ]
    assert available_under(menu, 10.0) == [menu[3], menu[0]]
    assert menu[0]["price"] == 8.0
    assert available_under(menu, 3.0) == []


def test_supplied_menu_available_items() -> None:
    assert [item["name"] for item in available_under(load_menu(), 10.0)] == [
        "Green Tea", "Edamame", "Gyoza (6 pc)", "Matcha Cheesecake",
    ]
