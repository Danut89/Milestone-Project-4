# 🧪 TESTING.md

## 🔍 Overview

This file documents the testing process for **FitZone Pro**, specifically covering manual and automated tests used to validate core functionality.

Both **manual tests** and **automated unit tests** were performed to ensure correctness, usability, and reliability across key parts of the platform.

---

## 🧪 Automated Unit Tests (Django TestCase)

Automated unit tests were written using Django’s built-in `TestCase` framework. These tests focus on the **Recipe** model and test key CRUD operations: create, update, and delete.

> All tests are located in:  
> `nutrition/tests.py`

### ✅ Test Class: `RecipeCRUDTests`

| Test Method | Purpose |
|-------------|---------|
| `test_create_recipe` | Ensures that a logged-in user can successfully create a recipe via POST request |
| `test_update_recipe` | Verifies that a user can update their own recipe and that the changes are saved |
| `test_delete_recipe` | Confirms that a user can delete a recipe and it is removed from the database |

### 🛠️ Setup Logic

Each test logs in a test user and uses the Django test client to simulate authenticated requests.

```python
def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testpass')
    self.client.login(username='testuser', password='testpass')
```

### Running the Tests

To execute all tests:

```bash
python manage.py test nutrition.tests.RecipeCRUDTests
```

### Test Output

All tests passed successfully. Output:

<details>
  <summary>📸 Test Output (Click to expand)</summary>

  ![Test Results](static/testing-screenshoots/test-results.png)

</details>


---


### ✅ Test Class: `GlobalSearchTests`

Automated tests were also written for the **Global Search** feature, which spans multiple apps (`shop`, `nutrition`, etc.).

> All tests are located in:  
> `home/tests.py`

| Test Method                         | Purpose |
|------------------------------------|---------|
| `test_results_page_returned`       | Verifies that a valid query returns the correct template and includes all matched objects (products, recipes, meal plans) in the context |
| `test_no_results_redirects_with_message` | Ensures that an unmatched search query redirects back and triggers a toast message saying `"No results found."` |

### 🛠️ Setup Logic

The tests simulate a logged-in user and create mock data for `Product`, `Recipe`, and `MealPlan`.

```python
def setUp(self):
    self.user = User.objects.create_user(username='tester', password='pass')
    self.product = Product.objects.create(name='Search Product', description='desc', price=9.99, category='equipment')
    self.recipe = Recipe.objects.create(title='Search Recipe', ingredients='i', instructions='i', prep_time_minutes=5, author=self.user)
    self.meal_plan = MealPlan.objects.create(title='Search Plan', description='d', calories=100, duration_days=7, created_by=self.user)
```

### Running the Tests

To execute all tests:

```bash
python manage.py test home.tests.GlobalSearchTests
```

### Test Output

All tests passed successfully. Output:

<details>
  <summary>📸 Test Output (Click to expand)</summary>

  ![Test Results](static/testing-screenshoots/test-results2.png)

</details>


---


### ✅ Test Class: `PasswordChangeTests`

This test suite verifies the **password change functionality** in the user settings section. It ensures the form behaves securely and correctly when changing passwords.

> All tests are located in:  
> `profiles/tests.py`

| Test Method              | Purpose |
|--------------------------|---------|
| `test_change_password_success` | Confirms that a logged-in user can successfully change their password using the password change form. Verifies the user stays logged in, the password is updated, and a success toast message is displayed. |

### 🛠️ Setup Logic

The test logs in a user with an initial password (`oldpass123`), submits a valid password change request, and confirms the update.

```python
def setUp(self):
    self.user = User.objects.create_user(username='tester', password='oldpass123')
    self.client.login(username='tester', password='oldpass123')

### Running the Tests

To execute all tests:

```bash
python manage.py test profiles.tests.PasswordChangeTests
```

### Test Output

All tests passed successfully. Output:

<details>
  <summary>📸 Test Output (Click to expand)</summary>

  ![Test Results](static/testing-screenshoots/test-results3.png)

</details>