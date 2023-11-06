from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
import plotly.express as px
from django.db.models import Sum
from calendar import month_name
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  
    
@login_required(login_url='/demo/')
def expense_list(request):
    # Get filter parameters from the request GET data
    category_filter = request.GET.get('category', None)
    month_filter = request.GET.get('month', None)
    location_filter = request.GET.get('location', None)

    # Get sorting parameter from the request GET data
    sort_by = request.GET.get('sort_by', None)

    # Query the expenses based on the filter parameters
    expenses = Expense.objects.all()
    if category_filter:
        expenses = expenses.filter(category=category_filter)
    if month_filter:
        expenses = expenses.filter(date__month=month_filter)
    if location_filter:
        expenses = expenses.filter(location=location_filter)

    # Sort the expenses based on the sorting parameter
    if sort_by == 'price_asc':
        expenses = expenses.order_by('amount')
    elif sort_by == 'price_desc':
        expenses = expenses.order_by('-amount')
    elif sort_by == 'date_asc':
        expenses = expenses.order_by('date')
    elif sort_by == 'date_desc':
        expenses = expenses.order_by('-date')

    # Calculate total expenses for the filtered data
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum']

    # Format total expenses with dollar sign and decimal places
    formatted_total_expenses = "${:.2f}".format(total_expenses) if total_expenses else None

    # Calculate total expenses per category
    category_expenses = expenses.values('category').annotate(total_expenses=Sum('amount'))
    categories = [expense['category'] for expense in category_expenses]

    # Get the unique months with data in the expenses
    months_with_data = expenses.dates('date', 'month')
    month_choices = [(month.month, month_name[month.month]) for month in months_with_data]

    # Get the unique locations with data in the expenses
    locations = expenses.values_list('location', flat=True).distinct()


    # Create a pie chart
    category_expenses = expenses.values('category').annotate(total_expenses=Sum('amount'))
    categories = [expense['category'] for expense in category_expenses]
    fig = px.pie(names=categories, values=[expense['total_expenses'] for expense in category_expenses], labels={'x': 'Category', 'y': 'Total Expenses'})
    chart_data = fig.to_json()
    
    return render(request, 'expense_tracker_app/expense_list.html', {
        'expenses': expenses,
        'chart_data': chart_data,
        'categories': categories,
        'month_choices': month_choices,
        'locations': locations,
        'total_expenses': formatted_total_expenses,  # Use formatted_total_expenses here
    })
    
@login_required(login_url='/demo/')
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expense_tracker_app/add_expense.html', {'form': form})

@login_required(login_url='/demo/')
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # Redirect to the home screen (expense_list view) after saving
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_tracker_app/edit_expense.html', {'form': form})

@login_required(login_url='/demo/')
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expense_tracker_app/delete_expense.html', {'expense': expense})

def get_demo_data():
    # Query all expenses for the demo view (without any filters)
    expenses = Expense.objects.all()

    # Get the unique months with data in the expenses
    months_with_data = expenses.dates('date', 'month')
    month_choices = [(month.month, month_name[month.month]) for month in months_with_data]

    # Get the unique locations with data in the expenses
    locations = expenses.values_list('location', flat=True).distinct()

    return expenses, month_choices, locations

def demo(request):
    if request.user.is_authenticated:
        return expense_list(request)
    else:
        expenses, month_choices, locations = get_demo_data()
        chart_data = None  

        return render(request, 'expense_tracker_app/expense_list.html', {
            'expenses': expenses,
            'chart_data': chart_data,
            'categories': [],  
            'month_choices': month_choices,
            'locations': locations,
            'total_expenses': None,  
        })