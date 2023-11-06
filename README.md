## Expense Tracker
The Expense Tracker is a Django web application that allows users to track and manage their expenses. It provides various features for adding, editing, and visualizing expenses.

## Features
- Expense Tracking: Users can add, view, edit, and remove expenses by specifying the date, category, amount, description, and location.

- Visualization: The application provides pie chart visualizations of expenses based on categories, allowing users to gain insights into their spending habits.

- Filter and Sort: Users can filter expenses based on category, location, and month. Expenses can also be sorted by date or amount in ascending or descending order.

## Requirements
To run this application, you need the following dependencies:

- Python 3.7+
- Django 3.2+
- Plotly Express (for data visualization)
- https://www.creative-tim.com/product/black-dashboard-pro-django/?AFFILIATE=52980 (Django theme that is used)

## Installation
1. Clone the repository:
git clone https://github.com/your-username/expense-tracker.git

2. Navigate to the project directory:
cd expense-tracker

3. Install the required dependencies

4. Set up the database:
  - python manage.py migrate
  - Create a superuser (admin) account:
  - python manage.py createsuperuser

5. Start the development server:
python manage.py runserver
Access the application in your web browser at http://localhost:8000.

## Usage
- Visit the home page to see your expense list and pie chart visualization.

- Click on "Add Expense" to add a new expense with the required details.

- Click on "Edit" or "Delete" next to any expense to modify or remove it.

- Use the filter and sort options to customize your expense list.

## Screenshots

![Screenshot 2023-11-06 175233](https://github.com/JoshL1206/Expense-Tracker-Website/assets/110563327/76c981af-2554-420f-8e33-3b8b2bb7d533)
![Screenshot 2023-11-06 175306](https://github.com/JoshL1206/Expense-Tracker-Website/assets/110563327/70e52a59-b59b-4773-8765-5ae31be86332)
![Screenshot 2023-11-06 175312](https://github.com/JoshL1206/Expense-Tracker-Website/assets/110563327/fc341bdf-a14e-489e-a90b-cb5d7e2fc02a)
![Screenshot 2023-11-06 175317](https://github.com/JoshL1206/Expense-Tracker-Website/assets/110563327/7e42cd6f-69ee-41c8-ab52-879fce5477d3)
![Screenshot 2023-11-06 175320](https://github.com/JoshL1206/Expense-Tracker-Website/assets/110563327/3cc08d2f-629e-4a05-bd32-a04ee7ba3c8d)
