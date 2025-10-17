from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction, Category
from .forms import TransactionForm, CategoryForm
from django.contrib.auth.decorators import login_required

import csv
from django.http import HttpResponse

from .utils import convert_currency


# List transactions
@login_required
# List transactions
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    # Check if a target currency is selected in GET parameters
    target_currency = request.GET.get('currency', 'USD')

    # Add converted_amount attribute to each transaction if currency is selected
    if target_currency:
        for tx in transactions:
            # convert_currency(amount, from_currency, to_currency)
            # assuming all transactions are in USD
            tx.converted_amount = convert_currency(tx.amount, 'USD', target_currency)

    context = {
        "transactions": transactions,
        "selected_currency": target_currency
    }
    return render(request, "transactions/transaction_list.html", context)

# Add transaction
@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm()
    return render(request, "transactions/transaction_form.html", {"form": form, "title": "Add Transaction"})

# Edit transaction
@login_required
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm(instance=transaction)
    return render(request, "transactions/transaction_form.html", {"form": form, "title": "Edit Transaction"})

# Delete transaction
@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        transaction.delete()
        return redirect("transaction_list")
    return render(request, "transactions/transaction_confirm_delete.html", {"transaction": transaction})



import csv
from django.http import HttpResponse

def export_transactions_csv(request):
    transactions = Transaction.objects.filter(user=request.user)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Category', 'Type', 'Amount', 'Description'])

    for tx in transactions:
        writer.writerow([tx.date, tx.category, tx.transaction_type, tx.amount, tx.description])

    return response
