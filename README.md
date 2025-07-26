# Milestone-Project-4

# 📚 Table of Contents

- [📖 About](#📖-about)
  - [ Project Overview](#project-overview)
  - [ Site Purpose](#site-purpose)
  - [🎯 Target Audience](#🎯-target-audience)
- [ User Experience (UX)](#user-experience-ux)
  - [✅ User Stories](#✅-user-stories)
  - [🎨 Design Choices](#🎨-design-choices)
    - [ Colour Palette](#colour-palette)
    - [ Typography](#typography)
    - [ Icons](#icons)
    - [ Animations and Interactivity](#animations-and-interactivity)
    - [ Responsive Design](#responsive-design)
  - [🧾 Wireframes](#🧾-wireframes)
- [💡 Features](#💡-features)
  - [ Navigation Bar](#navigation-bar)
  - [ Homepage](#homepage)
  - [ Authentication (Login / Signup)](#authentication-login--signup)
  - [ Recipe CRUD (Create, Read, Update, Delete)](#recipe-crud-create-read-update-delete)
  - [ Meal Plan Pages](#meal-plan-pages)
  - [ Product Catalog & Shop](#product-catalog--shop)
  - [ Cart & Checkout](#cart--checkout)
  - [ Orders & Order History](#orders--order-history)
  - [💚 Wishlist System](#💚-wishlist-system)
  - [ User Profiles & Dashboard](#👤-user-profiles--dashboard)
  - [ Admin Features](#admin-features)
  - [ Contact Page](#contact-page)
- [🖥️ Technologies Used](#🖥️-technologies-used)
  - [ Languages and Frameworks](#languages-and-frameworks)
  - [ Libraries and Packages](#libraries-and-packages)
  - [ Development Tools](#development-tools)
- [📐 Code Quality](#📐-code-quality)
- [ Database](#database)
  - [ Model Relationships](#model-relationships)
  - [ Schema Diagram](#schema-diagram)
- [🧪 Testing](#🧪-testing)
- [ Security](#-security)
- [ Deployment](#-deployment)
  - [ Render Deployment](#-render-deployment)
  - [ Cloning and Running Locally](#-cloning-and-running-locally)
- [🔧 Future Improvements](#-future-improvements)
- [📚 Credits](#-credits)
  - [ Resources and Tutorials](#-resources-and-tutorials)
  - [🙏 Inspiration and Acknowledgements](#-inspiration-and-acknowledgements)


## 📖 About

**Project Name**: FitZone Pro  
**Developer**: Danut Grigore  
**Type**: Milestone 4 – Full Stack Web Development (Code Institute)

FitZone Pro is a wellness-focused full-stack web application that allows users to discover meal plans, track recipes, shop fitness products, and manage their personal dashboard — all in one integrated platform.

Built using Django, PostgreSQL, and Bootstrap, it offers a responsive and professional user experience on any device.

---

###  Project Overview

FitZone Pro enables users to:

- 🥗 Explore curated meal plans tailored to different goals (e.g., weight loss, vegan, high-protein)
- 📖 View and manage healthy recipes, including adding their own
- 🛒 Shop for workout equipment, supplements, and clothing
- 👤 Save favorite items and track recent activity via a dashboard
- 🔐 Manage account information, including updating passwords and delivery preferences

Admins can add/edit products, review orders, and moderate recipe content via elevated permissions.

FitZone Pro is built to replicate real-world full-stack project challenges, including:

- User authentication & profile control
- CRUD operations across multiple models
- Stripe integration for e-commerce
- Clean, responsive frontend with custom styling
- Modular Django app structure

---

###  Site Purpose

The purpose of this project is to combine the most common tools used by fitness-focused users into one seamless digital experience. Unlike isolated meal plan apps or static recipe sites, FitZone Pro is designed to be:

- 💪 Goal-oriented
- 📱 Easy to use and mobile-friendly
- 🎯 Highly interactive for logged-in users
- 🛍️ Commercially capable through its integrated shop

The platform supports both anonymous browsing and rich personalized features for registered users. It encourages healthy habits while offering flexibility and control.

**Key Features Include:**

- ✅ Personalized user dashboard with saved content
- 🧾 Meal plan and recipe CRUD functionality
- 🛍️ Product catalog with cart and secure checkout
- 📦 Order tracking and past order display
- 💬 Feedback via toasts and validation
- 🔐 Secure profile & password management

---

### 🎯 Target Audience

FitZone Pro is designed for the following user groups:

- 🧍‍♂️ **Health-conscious individuals** who want to follow structured meal plans and track progress
- 🍳 **Home cooks and food enthusiasts** looking to discover or save healthy recipes
- 💪 **Fitness lovers** interested in buying quality supplements, gym gear, or workout apparel
- 👩‍💻 **Registered users** who want to personalize their wellness experience, save content, and manage their data securely
- 🛍️ **Shoppers** who want a convenient, all-in-one platform for browsing and purchasing fitness products
- 🛠️ **Admin users** responsible for managing content, monitoring orders, and maintaining site integrity

---

## User Experience UX

### ✅ User Stories

The following user stories were considered during the design and development of FitZone Pro:

#### 🧍 Guest User
- As a visitor, I want to explore the website without creating an account.
- As a visitor, I want to browse meal plans and recipes to decide if the platform suits me.
- As a visitor, I want to view and search by keyword available products before deciding to sign up.

#### 👤 Registered User
- As a user, I want to register and log in securely.
- As a user, I want to view and save my favorite recipes and meal plans.
- As a user, I want to manage my profile information and change my password.
- As a user, I want to add items to my cart and complete a secure checkout.
- As a user, I want to view my past orders and track my activity.

#### 🛠 Admin User
- As an admin, I want to add, update, and remove products in the shop.
- As an admin, I want to manage submitted recipes or plans if moderation is needed.
- As an admin, I want to monitor and process user orders.

Each user type was considered in the platform's navigation, available features, and access permissions.

---

### 🎨 Design Choices

This section will outline the visual and interaction design decisions made for FitZone Pro.

####  Colour Palette

> Placeholder: A clean and modern color palette was chosen to align with the brand identity and health/fitness focus. (Details to be added)

####  Typography

> Placeholder: The chosen fonts aim for readability, modern appeal, and consistency across devices. (Details to be added)

####  Icons

> Placeholder: Iconography enhances scannability and helps users identify sections intuitively. (Details to be added)

####  Animations and Interactivity

> Placeholder: Subtle animations, hover effects, and transitions were used to provide feedback and improve user experience. (Details to be added)

####  Responsive Design

> Placeholder: All templates were built mobile-first and thoroughly tested for responsiveness across device sizes. (Details to be added)

---

### 🧾 Wireframes

> Placeholder: Initial low-fidelity wireframes were created to define structure and layout before development began. Screenshots or links to mockups will be added here.

---

## 💡 Features

FitZone Pro is a wellness-focused web application that includes personalized dashboards, CRUD features, e-commerce integration, and a modular layout. This section outlines each major feature along with preview images.

---

### Navigation Bar

- Sticky top navigation with dropdowns for Recipes, Meal Plans, Shop, and Profile
- Adapts for mobile with collapsible menu
- Dynamic content: links change based on authentication state (Login/Register vs Dashboard/Logout)
- Includes site logo, search bar, and cart icon with item count

<details>
  <summary>📸 View Navigation Bar</summary>

![Navigation Bar](static/readme-screenshots/navbar-preview.png)

</details>

---

### Homepage

- Hero banner with brand message and call to action
- Sections: Featured Meal Plans, Benefits, Testimonials, and “How It Works”
- Uses gradient backgrounds, icons, and card-based layouts
- Built fully responsive for all screen sizes

<details>
  <summary>📸 View Homepage</summary>

![Homepage Preview](static/readme-screenshots/homepage-preview.png)

</details>

---

### Authentication (Login / Signup)

- Django built-in auth extended with custom login and registration forms
- Includes success/error toasts and redirection
- Forgot password and change password supported
- Secure access to private pages and personalized data

<details>
  <summary>📸 View Auth Pages</summary>

![Login](static/readme-screenshots/login-preview.png)

</details>

---

### Recipe CRUD (Create/ Read/ Update/ Delete)

- Recipes can be added, edited, and deleted by logged-in users
- Rich content including image, ingredients, steps, and calories
- Accordion display on detail pages for improved UX
- Recipes can be saved to the wishlist

<details>
  <summary>📸 View Recipe Detail</summary>

![Recipe](static/readme-screenshots/recipe-detail-preview.png)

</details>

---

### Meal Plan Pages

- Browse curated multi-day meal plans
- Each plan shows calories, focus (e.g., Vegan, High-Protein), and duration
- Expandable day-by-day view showing linked recipes
- Save plans to wishlist

<details>
  <summary>📸 View Meal Plan</summary>

![Meal Plan](static/readme-screenshots/mealplan-preview.png)

</details>

---

### Product Catalog & Shop

- Browse products by category (Supplements, Equipment, Apparel)
- View product details and add items to cart
- Admins can add/edit/delete products
- Fully responsive product grid

<details>
  <summary>📸 View Shop</summary>

![Shop](static/readme-screenshots/shop-preview.png)

</details>

---

### Cart & Checkout

- Cart page shows all added items with quantity and price
- Modify quantities, remove items, or proceed to checkout
- Stripe-powered secure checkout form with delivery info
- On success, order is saved and confirmation is shown

<details>
  <summary>📸 View Cart & Checkout</summary>

![Checkout](static/readme-screenshots/checkout-preview.png)

</details>

---

### Orders & Order History

- All past orders stored and displayed in user dashboard
- Each order includes timestamp, total, and item list
- Admins can view all orders in Django Admin panel

<details>
  <summary>📸 View Order History</summary>

![Order History](static/readme-screenshots/order-history-preview.png)

</details>

---

### 💚 Wishlist System

- Save any recipe or meal plan with a single button
- Toggle between saved/unsaved state using icon
- View all saved items in dashboard
- Only one entry allowed per item per user (no duplicates)

<details>
  <summary>📸 View Wishlist</summary>

![Wishlist](static/readme-screenshots/wishlist-preview.png)

</details>

---

### 👤 User Profiles & Dashboard

- Dashboard shows saved items, recent activity, and account links
- Profile page allows updating delivery info and password
- Option to hide/show activity feed
- Personalized and responsive layout

<details>
  <summary>📸 View Dashboard</summary>

![Dashboard](static/readme-screenshots/dashboard-preview.png)

</details>

---

###  Admin Features

- Admins can manage products, orders, and optionally recipes
- All CRUD functionality available via Django Admin interface
- Restricted by Django’s built-in permission system

<details>
  <summary>📸 View Admin Panel</summary>

![Admin](static/readme-screenshots/admin-preview.png)

</details>

---

### Contact Page

- Clean contact form with name, email, and message
- Placeholder for optional email functionality
- Can be extended later to integrate with email API

<details>
  <summary>📸 View Contact Form</summary>

![Contact](static/readme-screenshots/contact-preview.png)

</details>

---

## 🖥️ Technologies Used

The FitZone Pro application was built using modern full-stack technologies, combining frontend and backend tools for an interactive, secure, and scalable experience.

---

###  Languages and Frameworks

- **Python 3.11** – Core backend language powering Django and business logic.
- **Django 4.2** – Full-stack MVC framework managing models, views, templates, and admin.
- **PostgreSQL** – Production-ready relational database system, hosted via ElephantSQL.
- **HTML5** – Semantic structure and layout for web pages.
- **CSS3** – Styling with custom themes, responsive design, and media queries.
- **JavaScript (ES6)** – Frontend interactivity, toast logic, and validation.
- **Bootstrap 5** – Utility-first CSS framework used for responsive layout, modals, and grid.

---

###  Libraries and Packages

- **Cloudinary** – Handles media upload and delivery (for user-submitted images).
- **Gunicorn** – WSGI server used in production.
- **dj-database-url** – Parses database URLs from environment variables (for PostgreSQL).
- **psycopg2-binary** – PostgreSQL database adapter for Django.
- **Whitenoise** – Serves static files efficiently in production.
- **Stripe** – Payment gateway used for secure online checkout.
- **crispy-forms** – Enhances Django form styling with Bootstrap integration.
- **django-allauth** – User authentication, registration, and social login handling (if used).
- **boto3 / django-storages** – (Optional, if AWS was used for media or static storage)

---

###  Development Tools

- **Git & GitHub** – Version control and remote repository hosting.
- **GitHub Projects / Issues** – Planning, feature tracking, and progress documentation.
- **Visual Studio Code** – Main IDE for development and debugging.
- **DrawSQL / dbdiagram.io** – ERD creation for model planning and database visualization.
- **Lucidchart / Figma** – Used to plan wireframes and mockups.
- **Heroku or Render** – Cloud deployment and CI/CD integration.
- **Chrome DevTools** – Inspecting frontend layout, performance, and responsiveness.
- **W3C Validators** – Checked code validity (HTML, CSS) for clean, compliant markup.
- **PEP8 / Flake8** – Ensured clean and consistent Python codebase.


> 💡 Many of these tools are also documented throughout the development process in commit messages, planning docs, and this README.

---

## 📐 Code Quality

Maintaining clean, consistent, and maintainable code was a priority throughout the development of FitZone Pro. The project adheres to best practices and standards in both frontend and backend development.

---

### 🧱 Project Structure

- Django’s default project layout was followed and extended with **modular apps**:
  - `nutrition`: recipes, meal plans, and wishlist
  - `shop`: product catalog and categories
  - `cart` / `orders`: e-commerce flow
  - `profiles`: user profile and settings
- Static files (CSS, JS, images) and templates are **organized by app** for scalability and clarity.
- Reusable components (cards, buttons, toasts) are styled via a central CSS system.

---

### 🔤 Naming Conventions & Consistency

- All file and folder names are lowercase and use hyphens or underscores for clarity.
- Models, views, forms, and functions use **descriptive and semantically meaningful names**.
- URL paths and template names are consistent and reflect the feature they belong to.
- HTML classes follow **BEM-style** naming when needed for clarity (e.g. `meal-card__header`).

---

### 📘 Readable & Documented Code

- Inline comments are added for complex logic or less obvious code blocks.
- Each major template, view, and model is preceded by a docstring or section comment.
- Python code conforms to **PEP8** style guide using Flake8 linter.
- HTML and CSS were validated using **W3C validators** with no critical issues remaining.

---

### 🛡️ Defensive Coding & Error Handling

- Input validation is handled at both form and model level using Django’s built-in validators.
- Forms return user-friendly error messages when validation fails.
- Views use `get_object_or_404()` and `try/except` blocks to prevent crashes and handle edge cases.
- Stripe checkout includes error catching and fallback user feedback.

---

### ⚖️ Separation of Concerns

- Views contain business logic only; template logic is kept clean and minimal.
- Templates are built using **Django template inheritance** (`base.html` layout).
- All styles are stored in `index.css`, `nutrition.css`, and `shop.css`, reducing inline clutter.
- JavaScript used only where necessary, in dedicated JS files (e.g. toasts, quantity update).


> 🧠 This clean, readable, and maintainable codebase supports long-term scalability and follows industry standards. Quality is further supported by a consistent Git commit history documenting feature additions, fixes, and testing.

---
## Database

### Application Data Overview

FitZone Pro is a wellness-focused full-stack web application designed around a relational PostgreSQL database. Its structured data supports core functionality such as:

- **Users**: Authentication, profile management, and dashboard preferences.
- **Recipes**: Meal components with ingredients, cooking steps, and metadata.
- **Meal Plans**: Multi-day structures combining recipes for personalized goals.
- **Wishlist**: Save recipes and plans to personal favorites.
- **Products & Categories**: Nutrition and fitness-related goods available for purchase.
- **Orders & Cart Items**: E-commerce features powered by Stripe integration.

All data is normalized and managed through Django ORM. Models are organized into distinct apps reflecting their domain logic (e.g. `nutrition`, `orders`, `profiles`).

---

### Model Relationships

The FitZone Pro backend is built on a normalized PostgreSQL database using Django ORM. The app is split into modular Django apps, each with its own set of models.

The data schema is structured around the following core relationships:

- **User & UserProfile**: A one-to-one link between Django's default `User` model and the extended `UserProfile` model, which stores delivery details and user preferences.
  
- **Meal Plans, Days & Recipes**: 
  - Each `MealPlan` consists of multiple `MealPlanDay` entries (One-to-Many).
  - Each `MealPlanDay` can include multiple `Recipe` objects via a join table `meal_plan_day_recipes` (Many-to-Many).
  
- **Wishlist**:
  - A user can save both `Recipe` and `MealPlan` objects to their `Wishlist`.
  - Each wishlist entry references a `User` and either a `Recipe` or a `MealPlan`.

- **Product & Category**: 
  - Each `Product` belongs to a `Category` (One-to-Many).
  - Products are displayed in the shop and used in both the cart and orders.

- **Cart System**: 
  - A `CartItem` is created when a user adds a product to their cart.
  - Each cart item references a `User` and a `Product`.

- **Orders & OrderItems**:
  - When a user checks out, an `Order` is created.
  - The `Order` contains multiple `OrderItem` objects, each of which references a `Product` and quantity.

These relationships allow for a scalable, real-world structure that supports complex user workflows, including saving meal plans, checking out orders, and customizing the user experience.

---

### Normalization and Integrity

- The schema is **fully normalized** to reduce redundancy and improve scalability.
- All **foreign key** relationships enforce **referential integrity**.
- Where relevant, **cascade delete** and `related_name` attributes are used for clarity.
- Indexed fields such as `user_id`, `date_created`, and `meal_plan_id` optimize filtering and performance.


> 💡 For a visual representation, refer to the [Schema Diagram](#schema-diagram).

---

### Schema Diagram

Below is the full Entity Relationship Diagram (ERD) showing how the models in FitZone Pro are connected. This includes user data, nutrition plans, wishlist system, and order processing:


<details>
  <summary>📸 See ERD (Click to expand)</summary>

![FitZone Pro ERD](static/readme-screenshoots/fitzone_pro_erd.png)

</details>

### 🔄 Key Relationships Summary

- **User ↔ UserProfile**: One-to-One  
- **MealPlan → MealPlanDay**: One-to-Many  
- **MealPlanDay ↔ Recipe**: Many-to-Many (through `meal_plan_day_recipes`)  
- **User ↔ Wishlist (↔ Recipe/MealPlan)**: One-to-Many with optional FK  
- **User → Order → OrderItems → Product**: Chain of One-to-Many relationships  
- **Product → Category**: One-to-Many  
- **CartItem**: Combines User + Product to represent active cart

---

### 📊 Table Overview

| Model           | Key Fields                              | Relationships                                      |
|------------------|------------------------------------------|----------------------------------------------------|
| **User**             | id, username, email                     | Links to Profile, Orders, CartItems, Wishlist      |
| **UserProfile**      | user (OneToOne)                         | Extends User with delivery info                    |
| **Recipe**           | id, name, description                   | M2M with MealPlanDay, FK in Wishlist               |
| **MealPlan**         | id, title, summary                      | O2M with MealPlanDay, FK in Wishlist               |
| **MealPlanDay**      | id, meal_plan_id, day_number            | M2M with Recipe via `meal_plan_day_recipes`        |
| **Wishlist**         | user, recipe (opt), meal_plan (opt)     | FK to User + optional FK to Recipe or MealPlan     |
| **Product**          | name, category, price                   | FK to Category, used in OrderItems and CartItems   |
| **Category**         | name                                    | O2M with Product                                   |
| **CartItem**         | user, product, quantity                 | Represents cart items linked to a user             |
| **Order**            | user, total, date_created               | O2M: User → OrderItems                             |
| **OrderItem**        | order, product, quantity                | FK to Product and Order                            |

---

###  Schema Support for Key Features

| Feature                    | Schema Element(s) Involved                  |
|----------------------------|---------------------------------------------|
| Authentication            | User, UserProfile                           |
| Recipe CRUD                | Recipe, User, Wishlist                      |
| Meal Planning              | MealPlan, MealPlanDay, Recipe               |
| Saved Items (Wishlist)     | Wishlist (custom logic for dual-type save) |
| Shop Items & Categories    | Product, Category                           |
| Cart & Checkout            | CartItem, Order, OrderItem                  |
| Dashboard Info             | UserProfile, Order, Wishlist                |

---

## 🧪 Testing

Testing was conducted throughout the development of FitZone Pro to ensure functionality, data integrity, responsiveness, and user experience.

A detailed breakdown of all test cases, tools, methods, and results is available in a separate file:

📄 [**View Full Testing Documentation → `Testing.md`**](Testing.md)

---