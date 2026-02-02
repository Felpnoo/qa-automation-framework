# 🧪 QA Automation Framework (E-commerce)

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Fast-45ba4b?style=for-the-badge)
![Status](https://img.shields.io/badge/CI%2FCD-Passing-green?style=for-the-badge)

**A robust, scalable Test Automation Framework designed for enterprise environments.**

## 🎯 Project Scope
This project demonstrates a professional QA architecture applied to the [Swag Labs](https://www.saucedemo.com/) e-commerce platform. It focuses on maintainability, reliability, and automated reporting.

## 🏗 Architecture: Page Object Model (POM)
Unlike simple scripts, this framework decouples test logic from UI selectors using the **Page Object Pattern**. This ensures that UI changes only require updates in one place (`/pages`), keeping tests clean and stable.

## 🛠 Tech Stack
- **Core:** Python & Playwright (Modern, fast, reliable execution).
- **Runner:** Pytest (with Fixtures and Parametrization).
- **CI/CD:** GitHub Actions (Tests run automatically on every Push).
- **Reporting:** HTML Reports with Screenshots on failure.

## 🚀 How to Run (NixOS / Linux)
```bash
# 1. Enter Environment
nix develop

# 2. Run Tests (Headless)
pytest

# 3. Run with UI (Headed)
pytest --headed --slowmo 500

## 📂 Structure
```tree
.
├── pages/           # Page Objects (Selectors & Actions)
├── tests/           # Test Cases (Business Logic)
├── .github/         # CI/CD Pipeline Configuration
└── flake.nix        # Reproducible Environment
```
Developed by Felipe Silva to demonstrate QA Engineering best practices.
