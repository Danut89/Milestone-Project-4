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
