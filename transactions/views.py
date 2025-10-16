from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction, Category
from .forms import TransactionForm, CategoryForm
from django.contrib.auth.decorators import login_required

# List transactions
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, "transactions/transaction_list.html", {"transactions": transactions})

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
