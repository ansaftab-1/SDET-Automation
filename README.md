# SauceDemo QA & Automated Test Suite

Automated testing suite and QA documentation for [SauceDemo](https://www.saucedemo.com) built using **Python**, **Selenium WebDriver**, and **Pytest** following the **Page Object Model (POM)** pattern.

---

## Project Structure

```text
Test-case/
├── pages/
│   ├── base_page.py        # Base WebDriver wrapper and dynamic explicit waits
│   ├── login_page.py       # Login page objects and actions
│   ├── inventory_page.py   # Product catalog and cart interactions
│   ├── cart_page.py        # Cart page objects and actions
│   └── checkout_page.py    # Checkout flow objects and actions
├── tests/
│   ├── test_login.py       # Flow 1: Login with valid credentials
│   ├── test_checkout.py    # Flow 2: Add item to cart and complete checkout
│   └── test_locked_out.py  # Flow 3: Login with locked-out user
├── conftest.py             # Pytest browser fixture setup (Headless Chrome)
├── requirements.txt        # Project dependencies
├── test-plan.md            # Comprehensive QA Test Plan
├── bug-report.md           # Empirical Bug Report (7 Bugs)
└── README.md               # Project documentation
```

---

## Prerequisites

- Python 3.10+
- Google Chrome browser

---

## Setup & Installation


1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running Tests

### Run all tests
```bash
pytest -v
```

### Run specific test flows
- **Flow 1: Login with valid credentials**
  ```bash
  pytest -v tests/test_login.py
  ```
- **Flow 2: Add to cart and complete checkout**
  ```bash
  pytest -v tests/test_checkout.py
  ```
- **Flow 3: Locked-out user verification**
  ```bash
  pytest -v tests/test_locked_out.py
  ```

---

## Documentation

- **[Test Plan (`test-plan.md`)]**: QA strategy, scope, test cases (`TC-01` to `TC-06`), and risk assessment.
- **[Bug Report (`bug-report.md`)]**: 7 verified defects with reproduction steps, severity, and evidence.
