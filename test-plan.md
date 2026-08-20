# Test Plan – SauceDemo E-Commerce Platform

**Project:** SauceDemo (Swag Labs)  
**URL:** https://www.saucedemo.com  
**Author:**  Ans (SDET)  
**Date:** August 20, 2026  

## 1. Scope

### 1.1 In Scope
We’re covering the main user flows on SauceDemo for the different user types:

- **Login & Session**
  - Valid logins for all user types
  - Invalid logins (wrong password, empty fields, locked-out user)
  - Logout from the sidebar menu

- **Product Catalog**
  - Product names, descriptions, images and prices display correctly
  - Sorting (Name A-Z / Z-A, Price Low-High / High-Low)
  - Going from inventory list to individual product pages

- **Cart**
  - Adding items from both inventory and product detail pages
  - Cart badge number updates correctly
  - Removing items from inventory, detail page and cart page

- **Checkout**
  - Step 1: Filling first name, last name and zip code
  - Step 2: Checking order summary, prices, tax and total
  - Final confirmation page after finishing the order

### 1.2 Out of Scope
- Real payment processing
- Backend/database or server load testing
- Footer social media links (Twitter, Facebook, LinkedIn)

---

## 2. Types of Testing

| Type | What we’re checking |
|------|---------------------|
| Functional | Core flows work as expected (login, add to cart, sort, checkout, etc.) |
| UI / Visual | Layout, images, prices, badges and buttons look correct |
| Negative | What happens with bad inputs (wrong password, empty fields, locked user) |
| Edge Cases | Page refresh with items in cart, same prices when sorting, fast remove clicks, special characters in name fields |
| Cross-browser | Chrome |

---

## 3. Test Environment

### Browsers & Viewports
- Chrome (latest) – 1920x1080 (main automation browser)

### Prerequisites
- Python 3.10+
- Selenium 4.15+ and Pytest
- Chrome + ChromeDriver (via webdriver-manager)

---

## 4. Test Data & Users

All users use the password: `secret_sauce`

| Username | Purpose |
|----------|---------|
| standard_user | Normal happy-path user. Everything should work. |
| locked_out_user | Should show the locked-out error message and stay on login page. |
| problem_user | Intentionally broken (wrong images, sorting issues, form problems, wrong product links). |
| performance_glitch_user | Has ~5 second delay on login/navigation. Useful for timeout testing. |

---

## 5. Test Cases

### TC-001: Valid Login
- **ID:** TC-001
- **Title:** Successful login with standard_user
- **Preconditions:** On login page
- **Steps:**
  1. Enter `standard_user`
  2. Enter `secret_sauce`
  3. Click Login
- **Expected:** Redirects to inventory.html, “Products” header is shown, 6 items are visible
- **Status:** PASS

---

### TC-002: Locked Out User
- **ID:** TC-002
- **Title:** Locked-out user cannot log in
- **Preconditions:** On login page
- **Steps:**
  1. Enter `locked_out_user`
  2. Enter `secret_sauce`
  3. Click Login
- **Expected:** Stays on login page and shows error: “Epic sadface: Sorry, this user has been locked out.”
- **Status:** PASS

---

### TC-003: Cart Badge Updates
- **ID:** TC-003
- **Title:** Cart counter increases and decreases correctly
- **Preconditions:** Logged in as standard_user
- **Steps:**
  1. Add Sauce Labs Backpack → badge should show 1
  2. Add Sauce Labs Bike Light → badge should show 2
  3. Remove Backpack → badge should go back to 1
- **Expected:** Badge count updates correctly
- **Status:** PASS

---

### TC-004: Full Checkout Flow
- **ID:** TC-004
- **Title:** Complete purchase from start to finish
- **Preconditions:** Logged in as standard_user
- **Steps:**
  1. Add Sauce Labs Backpack
  2. Go to cart
  3. Click Checkout
  4. Fill First Name “John”, Last Name “Doe”, Zip “90210”
  5. Click Continue
  6. Click Finish on the overview page
- **Expected:** Lands on checkout-complete.html and sees “Thank you for your order!”
- **Status:** PASS

---

### TC-005: Price Sorting (Low to High)
- **ID:** TC-005
- **Title:** Sort products by price ascending
- **Preconditions:** Logged in as standard_user
- **Steps:**
  1. Open the sort dropdown
  2. Select “Price (low to high)”
- **Expected:** Prices appear in order: $7.99, $9.99, $15.99, $15.99, $29.99, $49.99
- **Status:** PASS

---

### TC-006: Checkout Validation – Missing First Name
- **ID:** TC-006
- **Title:** Error when First Name is empty
- **Preconditions:** Logged in, item in cart, on checkout-step-one.html
- **Steps:**
  1. Leave First Name blank
  2. Enter Last Name “Doe” and Zip “90210”
  3. Click Continue
- **Expected:** Shows error “Error: First Name is required” and stays on the same page
- **Status:** PASS

---

## 6. Risk Areas

| Area | Risk | Impact | Notes |
|------|------|--------|-------|
| Checkout form (problem_user / error_user) | Critical | High | Input fields can get overwritten or not saved, blocking checkout |
| Sorting | High | Medium | Sorting is broken on problem_user and prices look wrong on visual_user |
| Product detail links | High | Medium | On problem_user some product titles open the wrong item |
| Remove from cart on detail page | High | High | Remove button doesn’t always update cart state on problem/error users |
| Performance glitch user | Medium | Medium | ~5s delay – tests need proper waits or they can time out |
