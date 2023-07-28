Expense Tracker
The Expense Tracker is a Django web application that allows users to track and manage their personal expenses. It provides various features for adding, editing, and visualizing expenses.

Features
Expense Tracking: Users can add, view, edit, and remove expenses by specifying the date, category, amount, description, and location.

Visualization: The application provides pie chart visualizations of expenses based on categories, allowing users to gain insights into their spending habits.

Filter and Sort: Users can filter expenses based on category, location, and month. Expenses can also be sorted by date or amount in ascending or descending order.

Requirements
To run this application, you need the following dependencies:

Python 3.7+
Django 3.2+
Plotly Express (for data visualization)
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/expense-tracker.git
Navigate to the project directory:
bash
Copy code
cd expense-tracker
Install the required dependencies:
Copy code
pip install -r requirements.txt
Set up the database:
Copy code
python manage.py migrate
Create a superuser (admin) account:
Copy code
python manage.py createsuperuser
Start the development server:
Copy code
python manage.py runserver
Access the application in your web browser at http://localhost:8000.
Usage
Visit the home page to see your expense list and pie chart visualization.

Click on "Add Expense" to add a new expense with the required details.

Click on "Edit" or "Delete" next to any expense to modify or remove it.

Use the filter and sort options to customize your expense list.

Screenshots
