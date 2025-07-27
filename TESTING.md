# 🧪 TESTING.md

## 🔍 Overview

This file documents the testing process for **FitZone Pro**, specifically covering manual and automated tests used to validate core functionality.

Both **manual tests** and **automated unit tests** were performed to ensure correctness, usability, and reliability across key parts of the platform.

---

## 🧪 Automated Unit Tests (Django TestCase)

Automated unit tests were written using Django’s built-in `TestCase` framework. These tests focus on the **Recipe** model and test key CRUD operations: create, update, and delete.


### ✅ Test Class: `RecipeCRUDTests`

> tests are located in:  
> `nutrition/tests.py`

| Test Method | Purpose |
|-------------|---------|
| `test_create_recipe` | Ensures that a logged-in user can successfully create a recipe via POST request |
| `test_update_recipe` | Verifies that a user can update their own recipe and that the changes are saved |
| `test_delete_recipe` | Confirms that a user can delete a recipe and it is removed from the database |

#### 🛠️ Setup Logic

```python
def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testpass')
    self.client.login(username='testuser', password='testpass')
```

#### ▶️ Running the Tests

```bash
python manage.py test nutrition.tests.RecipeCRUDTests
```

<details>
  <summary>📸 Test Output (Click to expand)</summary>

  ![Test Results](static/testing-screenshoots/test-results.png)

</details>

---

### ✅ Test Class: `GlobalSearchTests`

> tests are located in:  
> `home/tests.py`

| Test Method                         | Purpose |
|------------------------------------|---------|
| `test_results_page_returned`       | Valid query returns correct template with all matched objects (products, recipes, meal plans) |
| `test_no_results_redirects_with_message` | Unmatched search query redirects with a toast saying `"No results found."` |

#### 🛠️ Setup Logic

```python
def setUp(self):
    self.user = User.objects.create_user(username='tester', password='pass')
    self.product = Product.objects.create(name='Search Product', description='desc', price=9.99, category='equipment')
    self.recipe = Recipe.objects.create(title='Search Recipe', ingredients='i', instructions='i', prep_time_minutes=5, author=self.user)
    self.meal_plan = MealPlan.objects.create(title='Search Plan', description='d', calories=100, duration_days=7, created_by=self.user)
```

#### ▶️ Running the Tests

```bash
python manage.py test home.tests.GlobalSearchTests
```

<details>
  <summary>📸 Test Output (Click to expand)</summary>

  ![Test Results](static/testing-screenshoots/test-results2.png)

</details>

---

### ✅ Test Class: `PasswordChangeTests`

> tests are located in:  
> `profiles/tests.py`

| Test Method              | Purpose |
|--------------------------|---------|
| `test_change_password_success` | Confirms user can change password successfully, remains logged in, and sees success toast |

#### 🛠️ Setup Logic

```python
def setUp(self):
    self.user = User.objects.create_user(username='tester', password='oldpass123')
    self.client.login(username='tester', password='oldpass123')
```

#### ▶️ Running the Tests

```bash
python manage.py test profiles.tests.PasswordChangeTests
```

<details>
  <summary>📸 Test Output (Click to expand)</summary>

  ![Test Results](static/testing-screenshoots/test-results3.png)

</details>


##  🔍 Manual Feature Testing

Manual testing was conducted across the major features of FitZone Pro using both desktop and mobile browsers. The following table outlines the results:

###  Features Manual Testing

| Feature                      | Tested On        | Expected Result                                             | Outcome   |
|-----------------------------|------------------|-------------------------------------------------------------|-----------|
| User Registration           | Desktop / Mobile | New user created, redirected to dashboard/home             | ✅ Pass    |
| Login / Logout              | Desktop / Mobile | User can log in, see account info, and securely log out     | ✅ Pass    |
| Create Recipe               | Desktop / Mobile | Recipe saved and appears in recipe list                     | ✅ Pass    |
| Edit / Delete Recipe        | Desktop / Mobile | User can update or delete their own recipe                  | ✅ Pass    |
| Save to Wishlist (Recipe)   | Desktop / Mobile | Wishlist button toggles and updates dashboard list          | ✅ Pass    |
| View Meal Plan Details      | Desktop / Mobile | Plan displays all days and meals; accordion works correctly | ✅ Pass    |
| Save to Wishlist (Meal Plan)| Desktop / Mobile | Toggle saves plan and appears in dashboard                  | ✅ Pass    |
| Add to Cart                 | Desktop / Mobile | Product added to cart and item count updates                | ✅ Pass    |
| Checkout Flow               | Desktop / Mobile | Stripe form loads, payment succeeds, order is saved         | ✅ Pass    |
| View Past Orders            | Desktop / Mobile | Orders show in dashboard with correct info                  | ✅ Pass    |
| Profile Info Update         | Desktop / Mobile | Address details update with success toast                   | ✅ Pass    |
| Password Change             | Desktop / Mobile | Password changes securely and user remains logged in        | ✅ Pass    |
| Admin Product Edit/Delete   | Desktop          | Product list updates immediately for admin users            | ✅ Pass    |

---

### 🧭 UI & Navigation Manual Testing

This section outlines tests for general navigation, link behavior, and UI feedback.

| Interaction Tested            | Action Performed                                | Expected Behavior                                       | Outcome   |
|-------------------------------|--------------------------------------------------|----------------------------------------------------------|-----------|
| Navigation Links              | Clicked: "Home", "Meal Plans", "Shop", "Dashboard" | Correct pages load and scroll to top                    | ✅ Pass    |
| Logo Click                    | Click logo from any page                         | Redirects to homepage                                   | ✅ Pass    |
| Dashboard Button              | Clicked avatar/profile icon                      | Opens dashboard if logged in                            | ✅ Pass    |
| Wishlist Tabs Toggle          | Click between Recipes / Meal Plans tabs          | Each tab shows relevant saved items                     | ✅ Pass    |
| Cart Icon Click               | Clicked from navbar                              | Opens cart page with current items                      | ✅ Pass    |
| Quantity Adjust Buttons       | Clicked plus/minus on cart page                  | Quantity updates and subtotal recalculates              | ✅ Pass    |
| Toast Message Dismiss         | Clicked close button on success/error toast      | Toast disappears                                         | ✅ Pass    |
| Scroll To Section             | Used nav or in-page anchor link (e.g. How It Works) | Page scrolls smoothly to anchor section                 | ✅ Pass    |
| Accordion (Meal Plan)         | Clicked each day in meal plan detail             | Expands/collapses correctly                             | ✅ Pass    |
| Responsive Menu Toggle        | Used hamburger icon on mobile view               | Expands and collapses menu                              | ✅ Pass    |
