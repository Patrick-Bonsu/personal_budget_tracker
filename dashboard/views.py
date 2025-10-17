from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import Transaction
from django.db.models import Sum
from datetime import datetime

@login_required
def dashboard_view(request):
    user_transactions = Transaction.objects.filter(user=request.user)

    # Calculate totals
    total_income = user_transactions.filter(transaction_type='Income').aggregate(total=Sum('amount'))['total'] or 0
    total_expense = user_transactions.filter(transaction_type='Expense').aggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expense

    # Optional: monthly aggregation for chart
    monthly_data = user_transactions.extra(select={'month': "strftime('%%Y-%%m', date)"}).values('month').annotate(
        income=Sum('amount', filter=models.Q(transaction_type='Income')),
        expense=Sum('amount', filter=models.Q(transaction_type='Expense'))
    ).order_by('month')

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'monthly_data': monthly_data
    }
    return render(request, "dashboard/dashboard.html", context)
