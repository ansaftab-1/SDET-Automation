# Bug Report — SauceDemo E-Commerce Platform

**Project:** SauceDemo (Swag Labs) Defect Documentation  
**Target URL:** [https://www.saucedemo.com](https://www.saucedemo.com)  
**Author:** Ans QA   
**Date:** August 20, 2026  

This report documents **7 distinct, non-obvious, empirically verified defects** identified during systematic exploratory and automated testing of the SauceDemo web application.

---

## Summary Matrix of Identified Defects

| Bug ID | Title / Summary | Affected User Role | Severity | Component |
|---|---|---|---|---|
| **BUG-001** | All product catalog images render broken fallback image asset (`sl-404.jpg`) | `problem_user` | **High** | Catalog / Media |
| **BUG-002** | Inventory dropdown sorting controls fail to reorder products | `problem_user` | **Medium** | Catalog / Sorting |
| **BUG-003** | Checkout Step 1 Last Name field overwrites First Name & blocks submission | `problem_user` | **Critical** | Checkout / Form State |
| **BUG-004** | Inventory product title href links redirect to wrong product detail page IDs | `problem_user` | **High** | Catalog / Router |
| **BUG-005** | Item Detail Page "Remove" button fails to update cart state or badge | `error_user` | **High** | Cart / Detail Page |
| **BUG-006** | Checkout Step 2 "Finish" button fails to complete order and locks progression | `error_user` | **Critical** | Checkout / Order API |
| **BUG-007** | Inventory sorting (Low to High) displays distorted, unsorted price values | `visual_user` | **Medium** | Catalog / Display |

---

## Detailed Bug Reports

### BUG-001: All product catalog images render broken fallback image asset (`sl-404.jpg`)

- **Bug ID:** `BUG-001`
- **Severity:** **High** (Degrades visual user experience and product identification)
- **Component:** Product Catalog Grid
- **User Account Found Under:** `problem_user`
- **Summary:** When logged in as `problem_user`, all product catalog items display the same broken dog image asset (`/assets/sl-404-Cq1a9k9X.jpg`) instead of their respective product photos (Backpack, Bike Light, etc.).
- **Steps to Reproduce:**
  1. Open `https://www.saucedemo.com/`.
  2. Log in with username `problem_user` and password `secret_sauce`.
  3. Observe the inventory items grid.
  4. Inspect the `src` attribute of each `img` tag inside `.inventory_item_img`.
- **Expected Result:** Each product item displays its specific, high-resolution product image asset.
- **Actual Result:** Every product item renders the 404 broken dog image asset: `src="/assets/sl-404-Cq1a9k9X.jpg"`.
- **Evidence Reference:** DOM attribute inspection confirms `img.src` is `/assets/sl-404-Cq1a9k9X.jpg` across all 6 product elements.

---

### BUG-002: Inventory dropdown sorting controls fail to reorder products

- **Bug ID:** `BUG-002`
- **Severity:** **Medium** (Core catalog sorting functionality completely non-functional)
- **Component:** Product Catalog Sorting
- **User Account Found Under:** `problem_user`
- **Summary:** Changing the product sorting select dropdown to "Name (Z to A)" or "Price (low to high)" fails to trigger any DOM reordering or array state update for `problem_user`.
- **Steps to Reproduce:**
  1. Log in as `problem_user`.
  2. On `inventory.html`, locate the dropdown select `[data-test="product-sort-container"]`.
  3. Change selection from `Name (A to Z)` to `Name (Z to A)` (`za`).
  4. Inspect product title order on screen.
  5. Change selection to `Price (low to high)` (`lohi`).
- **Expected Result:** Products reorder dynamically (Z to A starts with "Test.allTheThings() T-Shirt"; Low to High starts with $7.99 item).
- **Actual Result:** Products remain stuck in default order starting with "Sauce Labs Backpack" ($29.99). The dropdown value changes visually, but the underlying product list remains completely static.

---

### BUG-003: Checkout Step 1 Last Name field overwrites First Name & blocks submission

- **Bug ID:** `BUG-003`
- **Severity:** **Critical** (Prevents users from completing the purchase flow)
- **Component:** Checkout Step 1 (`checkout-step-one.html`)
- **User Account Found Under:** `problem_user`
- **Summary:** Inputting a value into the "Last Name" field during checkout inadvertently overwrites the "First Name" field and leaves the "Last Name" field empty, causing form submission to fail with `"Error: Last Name is required"`.
- **Steps to Reproduce:**
  1. Log in as `problem_user`.
  2. Add any item to the cart and navigate to `https://www.saucedemo.com/checkout-step-one.html`.
  3. Enter `"Alice"` into the First Name field (`[data-test="firstName"]`).
  4. Enter `"Smith"` into the Last Name field (`[data-test="lastName"]`).
  5. Inspect the DOM input values before submitting.
  6. Click the `Continue` button.
- **Expected Result:** First Name retains `"Alice"`, Last Name retains `"Smith"`, and form proceeds to `checkout-step-two.html`.
- **Actual Result:** First Name becomes `"Smith"`, Last Name is emptied (`""`). Clicking `Continue` displays error: `"Error: Last Name is required"`, completely blocking checkout.

---

### BUG-004: Inventory product title href links redirect to wrong product detail page IDs

- **Bug ID:** `BUG-004`
- **Severity:** **High** (Routing defect causing incorrect product item detail loading)
- **Component:** Product Router / Navigation
- **User Account Found Under:** `problem_user`
- **Summary:** Clicking on a specific product title on the main inventory grid navigates to a product detail page for a different product ID altogether.
- **Steps to Reproduce:**
  1. Log in as `problem_user`.
  2. On `inventory.html`, click on the title "Sauce Labs Backpack" (which is item ID `4`).
  3. Observe the URL and page content loaded.
- **Expected Result:** Browser navigates to `https://www.saucedemo.com/inventory-item.html?id=4` displaying Sauce Labs Backpack.
- **Actual Result:** Browser navigates to `https://www.saucedemo.com/inventory-item.html?id=5` displaying "Sauce Labs Fleece Jacket".

---

### BUG-005: Item Detail Page "Remove" button fails to update cart state or badge

- **Bug ID:** `BUG-005`
- **Severity:** **High** (Cart state inconsistency and failure to remove items)
- **Component:** Product Detail Page / Shopping Cart State
- **User Account Found Under:** `error_user`
- **Summary:** Adding an item to cart and then navigating to its Item Detail page to click "Remove" fails to remove the item from the cart state or decrement the shopping cart badge counter.
- **Steps to Reproduce:**
  1. Log in as `error_user`.
  2. Click `Add to cart` on "Sauce Labs Backpack". Observe cart badge displays `1`.
  3. Click on "Sauce Labs Backpack" title to open `inventory-item.html?id=4`.
  4. Click the `Remove` button (`[data-test="remove"]`).
  5. Check the cart badge icon counter in the header.
- **Expected Result:** Item is removed from cart, `Remove` button toggles back to `Add to cart`, and shopping cart badge counter disappears/decrements to `0`.
- **Actual Result:** Button click produces no state change; cart badge remains `1` and item stays in cart.

---

### BUG-006: Checkout Step 2 "Finish" button fails to complete order and locks progression

- **Bug ID:** `BUG-006`
- **Severity:** **Critical** (Total checkout process crash at final order submission)
- **Component:** Checkout Step 2 (`checkout-step-two.html`)
- **User Account Found Under:** `error_user`
- **Summary:** On the final order review step (`checkout-step-two.html`), clicking the "Finish" button fails to submit the order or navigate to `checkout-complete.html`. The application throws an exception and user remains trapped on Step 2.
- **Steps to Reproduce:**
  1. Log in as `error_user`.
  2. Add an item to cart and navigate through Checkout Step 1 to `checkout-step-two.html`.
  3. Click the `Finish` button (`[data-test="finish"]`).
- **Expected Result:** Order completes successfully; user is redirected to `https://www.saucedemo.com/checkout-complete.html` with message "Thank you for your order!".
- **Actual Result:** Page fails to navigate. Browser console/alert triggers an unhandled error and user remains stuck on `checkout-step-two.html`.

---

### BUG-007: Inventory sorting (Low to High) displays distorted, unsorted price values

- **Bug ID:** `BUG-007`
- **Severity:** **Medium** (Data corruption and visual display defect)
- **Component:** Catalog Display / Formatting
- **User Account Found Under:** `visual_user`
- **Summary:** When logged in as `visual_user` and sorting products by "Price (low to high)", product price tags display corrupted numerical values ($21.26, $56.78, $32.32) that fail mathematical ascending ordering rules.
- **Steps to Reproduce:**
  1. Log in as `visual_user`.
  2. Change product sort dropdown to `Price (low to high)`.
  3. Extract all product price values from `.inventory_item_price`.
- **Expected Result:** Prices sort in strictly ascending order ($7.99 < $9.99 < $15.99 < $15.99 < $29.99 < $49.99).
- **Actual Result:** Prices render as `$21.26`, `$56.78`, `$32.32`, which violates numerical ascending sorting ($56.78 > $32.32).
