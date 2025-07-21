# Milestone-Project-4

# 📚 Table of Contents

- [📖 About](#📖-about)
  - [🎯 Project Overview](#🎯-project-overview)
  - [🎯 Site Purpose](#🎯-site-purpose)
  - [🎯 Target Audience](#🎯-target-audience)
- [🧠 User Experience (UX)](#🧠-user-experience-ux)
  - [✅ User Stories](#✅-user-stories)
  - [🎨 Design Choices](#-design-choices)
    - [🎨 Colour Palette](#-colour-palette)
    - [🔤 Typography](#-typography)
    - [🔣 Icons](#-icons)
    - [🎞️ Animations and Interactivity](#-animations-and-interactivity)
    - [📱 Responsive Design](#-responsive-design)
  - [🧾 Wireframes](#-wireframes)
- [💡 Features](#-features)
  - [🏠 Homepage and Navigation](#-homepage-and-navigation)
  - [🔐 Authentication (Login / Signup)](#-authentication-login--signup)
  - [📋 Recipe CRUD (Create, Read, Update, Delete)](#-recipe-crud-create-read-update-delete)
  - [📸 Image Upload via Cloudinary](#-image-upload-via-cloudinary)
  - [🔎 Category Filtering and Search](#-category-filtering-and-search)
  - [❤️ Like/Favorite Recipes](#-likefavorite-recipes)
  - [💬 Comments](#-comments)
  - [🛠️ Admin Dashboard](#-admin-dashboard)
  - [🙍 User Profiles](#-user-profiles)
  - [📞 Contact Page](#-contact-page)
- [🛠 Technologies Used](#-technologies-used)
  - [💻 Languages and Frameworks](#-languages-and-frameworks)
  - [📦 Libraries and Packages](#-libraries-and-packages)
  - [🧰 Development Tools](#-development-tools)
- [📐 Code Quality](#-code-quality)
- [🗃 Database](#-database)
  - [🗺️ Schema Diagram](#-schema-diagram)
  - [🔗 Model Relationships](#-model-relationships)
- [🧪 Testing](#-testing)
- [🔐 Security](#-security)
- [🚀 Deployment](#-deployment)
  - [🔄 Render Deployment](#-render-deployment)
  - [💻 Cloning and Running Locally](#-cloning-and-running-locally)
- [🔧 Future Improvements](#-future-improvements)
- [📚 Credits](#-credits)
  - [📘 Resources and Tutorials](#-resources-and-tutorials)
  - [🙏 Inspiration and Acknowledgements](#-inspiration-and-acknowledgements)


# 📖 About

**Project Name**: FitZone Pro  
**Developer**: Danut Grigore  
**Type**: Milestone 4 – Full Stack Web Development (Code Institute)

FitZone Pro is a wellness-focused full-stack web application that allows users to discover meal plans, track recipes, shop fitness products, and manage their personal dashboard — all in one integrated platform.

Built using Django, PostgreSQL, and Bootstrap, it offers a responsive and professional user experience on any device.

---

## 🎯 Project Overview

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

## 🎯 Site Purpose

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

## 🎯 Target Audience

FitZone Pro is designed for the following user groups:

- 🧍‍♂️ **Health-conscious individuals** who want to follow structured meal plans and track progress
- 🍳 **Home cooks and food enthusiasts** looking to discover or save healthy recipes
- 💪 **Fitness lovers** interested in buying quality supplements, gym gear, or workout apparel
- 👩‍💻 **Registered users** who want to personalize their wellness experience, save content, and manage their data securely
- 🛍️ **Shoppers** who want a convenient, all-in-one platform for browsing and purchasing fitness products
- 🛠️ **Admin users** responsible for managing content, monitoring orders, and maintaining site integrity

---

## ✅ User Stories

The following user stories were considered during the design and development of FitZone Pro:

### 🧍 Guest User
- As a visitor, I want to explore the website without creating an account.
- As a visitor, I want to browse meal plans and recipes to decide if the platform suits me.
- As a visitor, I want to view available fitness products before deciding to sign up.

### 👤 Registered User
- As a user, I want to register and log in securely.
- As a user, I want to view and save my favorite recipes and meal plans.
- As a user, I want to manage my profile information and change my password.
- As a user, I want to add items to my cart and complete a secure checkout.
- As a user, I want to view my past orders and track my activity.

### 🛠 Admin User
- As an admin, I want to add, update, and remove products in the shop.
- As an admin, I want to manage submitted recipes or plans if moderation is needed.
- As an admin, I want to monitor and process user orders.

Each user type was considered in the platform's navigation, available features, and access permissions.
