# Personal Budget Tracker

A web-based application built with Django that helps users manage their personal finances by tracking income, expenses, categories, and generating dashboards with charts.

## Features

- **User Authentication:** Registration, login, logout
- **Transactions CRUD:** Create, view, update, delete transactions
- **Categories:** Assign transactions to categories
- **Dashboard:** View total income, expenses, balance, and monthly charts
- **Export:** Export transactions to CSV
- **Optional Currency Conversion:** Convert transaction amounts to different currencies

## Technology Stack

- **Backend:** Python 3.13, Django 5.2
- **Frontend:** HTML, CSS, Chart.js (for charts)
- **Database:** SQLite (default)
- **Version Control:** Git, GitHub

## Project Structure

personal_budget_tracker/
├── budget_tracker/ # Django project folder
├── dashboard/ # Dashboard app
├── transactions/ # Transactions app
├── users/ # User authentication app
├── templates/ # HTML templates
├── static/ # Static files (CSS, JS)
├── manage.py
└── requirements.txt


## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd personal_budget_tracker

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3. Install dependencies

```bash
pip install -r requirements.txt

4. Apply migrations

```bash
python manage.py migrate

5. Create a superuser (optional, for admin access:

```bash
python manage.py createsuperuser

6. Run the server

```bash
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.


Usage
1. Register a new account or login with an existing account.
2. Add transactions and assign categories.
3. View the dashboard for totals and charts.
4. Export your transactions to CSV.
5. (Optional) Convert currency using the dropdown in the transactions list.

Contributing
1. Fork the repository
2. Create a feature branch (git checkout -b feature/YourFeature)
3. Commit your changes (git commit -m "Add some feature")
4. Push to branch (git push origin feature/YourFeature)
5. Create a Pull Request