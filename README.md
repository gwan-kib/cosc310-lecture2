# COSC 310 Lecture 2: Python and Git

Restaurant menu filtering, a shopping cart, business-rule validation, and pytest tests.

## Setup and run (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python exercise1.py
python exercise2.py
python exercise3.py
python -m pytest -v
```

## Exercises

- `exercise1.py`: load the supplied JSON menu; show available items strictly below the price limit, cheapest first.
- `exercise2.py`: store cart lines as dictionaries, combine quantities by item ID, remove and clear lines, and round the total once at the end.
- `exercise3.py`: validate quantity and availability before changing the cart; reject removal of an absent item. The rules live in `Cart.add_item` and `Cart.remove_item`.
- `tests/test_cart.py`: check cart behavior and rejection cases.

The examples use the supplied menu. Although the starter docstring mentions Iced Coffee, it is unavailable in that menu and must not be printed.

## AI assistance disclosure

OpenAI Codex assisted with implementing the exercises, adding tests, writing documentation, and preparing the Git/GitHub workflow. The student must review and understand the implementation and is responsible for the submitted work.
