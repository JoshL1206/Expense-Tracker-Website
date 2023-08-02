## Expense Tracker
The Expense Tracker is a Django web application that allows users to track and manage their personal expenses. It provides various features for adding, editing, and visualizing expenses.

## Features
- Expense Tracking: Users can add, view, edit, and remove expenses by specifying the date, category, amount, description, and location.

- Visualization: The application provides pie chart visualizations of expenses based on categories, allowing users to gain insights into their spending habits.

- Filter and Sort: Users can filter expenses based on category, location, and month. Expenses can also be sorted by date or amount in ascending or descending order.

## Requirements
To run this application, you need the following dependencies:

- Python 3.7+
- Django 3.2+
- Plotly Express (for data visualization)

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
![f1beb59c5dc9d2c8e4fd8644dc300556](https://github.com/JoshL1206/Expense-Tracker-Website/assets/110563327/b7060c3b-b61c-4a47-937d-a99a0e228a90)
![908c4e6c99c396cd1a7700691b987516](https://github.com/JoshL1206/Expense-Tracker-Website/assets/110563327/8acfc6f1-1b3e-4dd1-91ca-29ae37a2d8fb)
![d3596567093bc3e4d1df600dd1e09111](https://github.com/JoshL1206/Expense-Tracker-Website/assets/110563327/1343271a-4013-4bb4-96be-2b28335c78b9)
![80e7df6ba5b2ce232ee593291203e5cb](https://github.com/JoshL1206/Expense-Tracker-Website/assets/110563327/1779c9ed-de3b-47ee-985b-15e206c51534)
