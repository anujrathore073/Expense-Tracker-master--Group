<h1 align="center">💰 Expense Tracker - Flask Web App</h1>

<p align="center">
  A simple and efficient web-based expense tracker to manage members, earnings, and expenses using Python Flask.
</p>

---

## 📸 Screenshots

<!-- Add screenshots like the homepage, add expense page, or dashboard -->
<p align="center">
  <img src="screenshots/dashboard.png" width="700" alt="Dashboard Screenshot" />
  <br/>
  <img src="screenshots/add-expense.png" width="700" alt="Add Expense Screenshot" />
</p>

---

## 🚀 Features

- 👥 Add and manage members
- 💵 Track individual earnings
- 🧾 Record categorized expenses
- ⚖️ Calculate real-time balances
- 📊 Overview of total income vs expenses
- 🌐 Simple, responsive web interface

---

## 🏗️ Tech Stack

| Layer         | Technology           |
|---------------|----------------------|
| Backend       | Python, Flask         |
| Frontend      | HTML, CSS, Bootstrap  |
| Database      | SQLite (via SQL queries) |
| Templates     | Jinja2 (Flask Templating) |

---

## 📁 Project Structure

```bash
Expense-Tracker/
│
├── app.py               # Main Flask application
├── config.py            # Database config and setup
├── queries.sql          # SQL table creation script
├── requirements.txt     # Python dependencies
│
├── static/              # CSS, JS, Images
│   └── style.css
│
└── templates/           # Jinja2 HTML templates
    ├── index.html
    ├── add_member.html
    ├── add_expense.html
    └── ...
